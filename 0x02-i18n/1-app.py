#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template
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


@app.route('/')
def hello_Hoblertoni():
    """
    simply outputs “Hello world”
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
