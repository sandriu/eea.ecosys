import flask
from flask.ext.assets import Environment, Bundle
from models import db

# import blueprints
from .library import library

from .assets import BUNDLE_JS, BUNDLE_CSS


DEFAULT_CONFIG = {
    'MONGODB_SETTINGS': {
        'DB': 'ecosys',
    },
    'ASSETS_DEBUG': True,
    'CSRF_ENABLED': False,
}

BLUEPRINTS = (
    library,
)


def create_app(instance_path=None, config={}):
    app = flask.Flask(__name__, instance_path=instance_path,
                      instance_relative_config=True)
    configure_app(app, config)
    configure_blueprints(app, BLUEPRINTS)
    configure_assets(app)
    db.init_app(app)
    return app


def configure_app(app, config):
    app.config.update(DEFAULT_CONFIG)
    app.config.from_pyfile('settings.py', silent=True)
    app.config.update(config)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_assets(app):
    assets = Environment(app)
    js = Bundle(*BUNDLE_JS, filters='jsmin', output='output/packed.js')
    css = Bundle(*BUNDLE_CSS, filters='cssmin', output='output/packed.css')

    assets.register('packed_js', js)
    assets.register('packed_css', css)