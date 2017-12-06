
import re
import urlparse
import urllib2
import time
from datetime import datetime
import robotparser
import Queue


def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp', proxy=None, num_retries=1):
    """Crawl from the giver seed URL following links matched by link_regex
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = Queue.deque([seed_url])
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}
    #track how many URL's have been downloaded
    num_urls = 0
    rp = get_robots(seed_url)
    throttle = Thorttle(delay)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent

    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                # add this link to the crawl queue
                crawl_queue.append(link)


def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com/places/default', '/(index|view)')