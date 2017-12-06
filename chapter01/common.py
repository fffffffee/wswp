

import urllib2

def download(url, user_agent='wswp', num_retries=2):
    """Download function that includes user agent support"""
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    #try:
    html = urllib2.urlopen(request).read()
    #except urllib2.URLError as e:
    #    print 'Download error:', e.reason
    #    html = None
    #    if num_retries > 0:
    #        if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
    #            html = download(url, user_agent, num_retries-1)
    return html

if __name__ == '__main__':
    print download('http://example.webscraping.com')