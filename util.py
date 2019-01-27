# -*- coding: utf-8 -*-

import requests
from ask_sdk_model import IntentRequest
from typing import Union, Dict, List


def get_article_by_keyword(article_data, keyword):
    """Return a article based on keyword."""
    # type: (Dict, str) -> str
    return [r for r in article_data["articles"] if keyword in r["keywords"]]


def get_article_by_name(article_data, title):
    """Return an article based on name."""
    # type: (Dict, str) -> Dict
    for r in article_data["articles"]:
        if r["title"] == name:
            return r
    return {}


def http_get(url, path_params=None):
    """Return a response JSON for a GET call from `request`."""
    # type: (str, Dict) -> Dict
    response = requests.get(url=url, params=path_params)

    if response.status_code < 200 or response.status_code >= 300:
        response.raise_for_status()
    return response.json()



def get_resolved_value(request, slot_name):
    """Resolve the slot name from the request."""
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return request.intent.slots[slot_name].value
    except (AttributeError, ValueError, KeyError, IndexError):
        return None
