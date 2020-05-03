import threading
from queue import Queue
import mongoUtil
from spider import spider

_homepage = "https://abcnews.go.com/"
_domain = "abcnews.go.com"
_links = set()
_num_threads = 10
_queue = Queue()
spider(_homepage, _domain)

def create_spiders():
    for _ in range(_num_threads):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = _queue.get()
        spider.crawl_page(threading.current_thread().name, url)
        _queue.task_done()

def create_jobs():
    for link in spider.queue:
        _queue.put(link)
    _queue.join()
    crawl()

def crawl():
    queue_links = spider.queue
    if len(queue_links) > 0:
        create_jobs()

def main():
    create_spiders()
    crawl()

if __name__ == '__main__':
    main()
