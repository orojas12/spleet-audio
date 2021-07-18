from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app(config=None):

    app = Flask(__name__)

    # set default config
    app.config.from_object('audiosplitter.default_config')
    
    # overrides default config if applicable
    if config is not None:
        app.config.from_pyfile(config)

    from . import routes
    app.register_blueprint(routes.bp)

    return app