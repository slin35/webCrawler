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

def main():
 ##   connector = mongoUtil.DBConnector()

#    finder.feed('<html><head><title></title></head></html>')

 #   utils.get_urls("https://abcnews.go.com/")
    pass

if __name__ == '__main__':
    main()
