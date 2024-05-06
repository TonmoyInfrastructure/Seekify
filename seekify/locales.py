import os
import flask
from flask.ctx import has_request_context
from pathlib import Path

LOCALE_NAMES = {}
RTL_LOCALES: set[str] = set()
ADDITIONAL_TRANSLATION = {

}


def select_locale():
    locale = 'en'
    if has_request_context():
        value = flask.request.preferences.get_value('locale')
        if value:
            locale = value