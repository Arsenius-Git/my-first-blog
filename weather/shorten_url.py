import pyshorteners
from django.conf import settings
from .forms import GetUrl

def shorten(url):
    url_short = pyshorteners.Shortener().tinyurl.short(url)
    return url_short