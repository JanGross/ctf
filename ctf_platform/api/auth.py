from flask import Blueprint, g, redirect, request, session, url_for, jsonify
from flask import current_app as app
from werkzeug.security import check_password_hash, generate_password_hash
from .database import get_db
from .helper_functions import build_response_dict
import functools
bp = Blueprint('auth', __name__, url_prefix='/auth/')



@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db = get_db()
        db.execute(
            'SELECT user_id, username, active, registered, info FROM user WHERE user_id = %s', (user_id)
        )
        g.user = db.fetchone()
        app.logger.info('USER ACCESS %s' % (g.user))

#@auth.login_required decorator
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwagrs):
        if g.user is None:
            api_response = build_response_dict(False, 'access', 'Access denied', reason='Login required')
            return jsonify(api_response)
        return view(**kwagrs)

    return wrapped_view

@bp.route("/register", methods=['POST'])
def register():
    api_response = {}
    error = None
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    if not username:
        error = 'Username required!'
    elif not password:
        error = 'Password required!'
    else:
        db.execute('SELECT user_id FROM user WHERE username = %s', (username))
        if db.fetchone():
            error = "Username already exists!"
    if error is None:
        password_hash = generate_password_hash(password)
        db.execute('INSERT INTO user (username, password) VALUES (%s, %s)', (username, password_hash))
        g.db.commit()
        api_response = build_response_dict(True, 'register', 'Registration successful')
    else:
        api_response = build_response_dict(False, 'register', 'Registration failed', reason=error)
    return jsonify(api_response)        

@bp.route("/login", methods=['POST'])
def login():
    api_response = {}
    error = None
    username = request.form.get('username')
    password = request.form.get('password')
    if not username:
        error = 'Username required!'
    elif not password:
        error = 'Password required!'
    else:
        db = get_db()
        db.execute("SELECT * FROM user WHERE username = %s", (username))
        db_user = db.fetchone()
        if db_user is None or not check_password_hash(db_user['password'], password):
            error = 'Username or password incorrect!'
    if error is None:
        session.clear()
        session['user_id'] = db_user['user_id']
        session['user_name'] = db_user['username'] 
        api_response = build_response_dict(True, 'login', 'Login successful')
        app.logger.info("{} logged in successfully!".format(username))
    else:
        api_response = build_response_dict(False, 'login', 'Login failed', reason=error)
        app.logger.info("{} failed to login ({})!".format(username, error))

    return jsonify(api_response)

@bp.route('/logout',  methods=['GET'])
def logout():
    if 'user_name' in session:
        app.logger.info("{} logged out!".format(session['user_name']))
        session.clear()
        api_response = build_response_dict(True, 'logout', 'Logout successful')
    else:
        api_response = build_response_dict(False, 'logout', 'Logout failed', reason='No active session')
    return jsonify(api_response)