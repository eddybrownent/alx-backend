#!/usr/bin/env python3
"""
Flask app
"""
from typing import Union, Dict
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    class to config Flask app
    has a LANGUAGES
    Babel’s default locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale() -> str:
    """
    determineS best match with supported languages
    """
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


def get_user(user_id: int) -> Union[Dict, None]:
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/')
def hello_Hoblerton() -> str:
    """
    simply outputs “Hello world”
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
