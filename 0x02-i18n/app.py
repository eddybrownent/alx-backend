#!/usr/bin/env python3
"""
Flask app
"""
from datetime import datetime
import pytz
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

    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']

    request_locale = request.headers.get('Accept-Language')

    if request_locale in app.config["LANGUAGES"]:
        return request_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Timezone from URL parameters
    """
    requested_timezone = request.args.get('timezone')
    try:
        if requested_timezone:
            _ = get_timezone(requested_timezone)
            return requested_timezone
    except Exception as e:
        pass

    if g.user and g.user and 'timezone' in g.user:
        try:
            _ = get_timezone(g.user['timezone'])
            return g.user['timezone']
        except Exception as e:
            pass

    return Config.BABEL_DEFAULT_TIMEZONE


# babel.init_app(app, locale_selector=get_locale,
#               timezone_selector=get_timezone)


def get_user(user_id: int) -> Union[Dict, None]:
    """
    Get user information based on user ID

    Args:
        user_id (int): The ID of the user to retrieve

    Returns:
        Union[Dict, None]]]: dict containing user infor
        or None if the user ID is not found
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    to find a user if any
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None
    g.timezone = get_timezone()


@app.route('/')
def hello_Hoblerton() -> str:
    """
    simply outputs “Hello world”
    """
    current_time = datetime.now(pytz.timezone(
        g.timezone)) if g.timezone else datetime.utcnow()

    formatted_time = current_time.strftime(
        '%b %d, %Y, %I:%M:%S %p'
        ) if get_locale() == 'en' else current_time.strftime(
            '%d %b %Y à %H:%M:%S')
    return render_template('index.html', formatted_time=formatted_time)


if __name__ == '__main__':
    app.run()
