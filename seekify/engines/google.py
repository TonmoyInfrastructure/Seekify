import babel
import typing
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import logging
    logger:logging.Logger
traits: EngineTraits

def get_from_google(params, engine_traits):
    return_value = {
        'language': None,
        'country': None,
        'subdomain': None,
        'params': {},
        'headers': {},
        'cookies': {},
        'locale': None,
    }


skfy_loc = params.get('seekify_locale', 'all')
try:
    locale = babel.Locale.parse(skfy_loc, sep='-')
except babel.core.UnknownLocaleError:
    locale = None

lang_english =
