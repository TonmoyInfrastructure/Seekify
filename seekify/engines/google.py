import babel


def get_from_google(params, eng_traits):
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
    locale = babel
