from urllib.request import urlopen
from linkFinder import linkFinder

class spider:
    base_url = ''
    domain_name = ''

    queue = set()
    crawled = set()

    def __init__(self, base_url, domain_name):
        spider.base_url = base_url
        spider.domain_name = domain_name
        spider.queue.add(base_url)
        self.crawl_page("first spider", spider.base_url)


    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_mongo()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")

            finder = linkFinder(spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print("cannot crawl page")
            return set()
        return finder.get_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            if spider.domain_name not in url:
                continue
            spider.queue.add(url)
    
    @staticmethod
    def update_mongo():
        pass







