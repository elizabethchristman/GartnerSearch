# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = "Gartner Magic Quadrant Search"

WELCOME = _("Welcome to Gartner Magic Quadrant Search")
HELP = _("Say a keyword to search for an article.")
ABOUT = _("Gartner Magic Quadrant research methodology provides a graphical competitive positioning of four types of technology providers in fast-growing markets: Leaders, Visionaries, Niche Players and Challengers.")
STOP = _("Okay, see you next time!")
FALLBACK = _("The {} can't help you with that. It can help you learn about Gloucester if you say tell me about this place. What can I help you with?")
GENERIC_REPROMPT = _("What can I help you with?")

ARTICLE_DATA = {
    "keywords": [
        {
            "title": "Zeke's Place",
            "authors": '66 East Main Street',
            "summary": '978-283-0474',
            
            "meals": 'breakfast, lunch',
            "description": 'A cozy and popular spot for breakfast.  Try the blueberry french toast!',
        },
        {
            "name": 'Morning Glory Coffee Shop',
            "address": '25 Western Avenue',
            "phone": '978-281-1851',
            "meals": 'coffee, breakfast, lunch',
            "description": 'A homestyle diner located just across the street from the harbor sea wall.',
        },
        {
            "name": 'Sugar Magnolias',
            "address": '112 Main Street',
            "phone": '978-281-5310',
            "meals": 'breakfast, lunch',
            "description": 'A quaint eatery, popular for weekend brunch.  Try the carrot cake pancakes.',
        },
        {
            "name": 'Seaport Grille',
            "address": '6 Rowe Square',
            "phone": '978-282-9799',
            "meals": 'lunch, dinner',
            "description": 'Serving seafood, steak and casual fare.  Enjoy harbor views on the deck.',
        },
        {
            "name": 'Latitude 43',
            "address": '25 Rogers Street',
            "phone": '978-281-0223',
            "meals": 'lunch, dinner',
            "description": 'Features artsy decor and sushi specials.  Live music evenings at the adjoining Minglewood Tavern.',
        },
        {
            "name": "George's Coffee Shop",
            "address": '178 Washington Street',
            "phone": '978-281-1910',
            "meals": 'coffee, breakfast, lunch',
            "description": 'A highly rated local diner with generously sized plates.',
        },
    ],
}

MY_API = {
    "host": "https://query.yahooapis.com",
    "port": 443,
    "path": "/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%2C%20{state}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys",
}
