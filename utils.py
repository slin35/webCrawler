from html.parser import HTMLParser
from urllib import parse
import requests
from bs4 import BeautifulSoup
from collections import deque

_queue = set()
_crawled = set()

def get_urls(fontier: str) -> dict:
    _queue.add(fontier)

