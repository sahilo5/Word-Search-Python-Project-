from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRETE_KEY'] = "jdkfjjkdjkfj"

    from .project import project

    app.register_blueprint(project, url_prefix ='/')

    return app