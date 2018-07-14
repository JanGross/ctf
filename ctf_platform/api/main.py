from flask import Flask, jsonify
import os, logging, sys

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.cfg')
    app.secret_key = os.urandom(24)
    from . import auth, database
    database.init_app(app)
    app.register_blueprint(auth.bp)

    @app.route("/")
    def home():
        info = { 'data' : { 'version': '1.0' }}
        return jsonify(info)

    return app