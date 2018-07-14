import pymysql, click, re
from flask import current_app as app
from flask import g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        mysql = pymysql.connect(host=app.config['MYSQL_DATABASE_HOST'], 
                                user=app.config['MYSQL_DATABASE_USER'],
                                password=app.config['MYSQL_DATABASE_PASS'],
                                db=app.config['MYSQL_DATABASE_DB'],
                                cursorclass=pymysql.cursors.DictCursor)
        g.db = mysql
        g.db_cursor = mysql.cursor()
    return g.db_cursor

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db(schema):
    db = mysql = pymysql.connect(host=app.config['MYSQL_DATABASE_HOST'], 
                                user=app.config['MYSQL_DATABASE_USER'],
                                password=app.config['MYSQL_DATABASE_PASS'])
    statement = ""
    for line in open(schema):
        if line.strip().startswith('--'):  # ignore sql comment lines
            continue
        if not line.strip().endswith(';'):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            try:
                db.cursor().execute(statement)
            except Exception as e:
                print("[WARN] MySQLError during execute statement \n\tArgs: '{}'".format(str(e.args)))
            statement = ""

@click.command('init-db')
@click.argument('schema')
@with_appcontext
def init_db_command(schema):
    init_db(schema)
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)