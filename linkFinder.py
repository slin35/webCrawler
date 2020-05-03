from html.parser import HTMLParser
from urllib import parse

class linkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attr, value) in attrs:
                if attr == 'href':
                    # properly format url when it is not properly formatted
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
    
    def get_links(self):
        return self.links


    

