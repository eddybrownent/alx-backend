#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


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
def get_locale():
    """
    determineS best match with supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def hello_Hoblerton():
    """
    simply outputs “Hello world”
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
