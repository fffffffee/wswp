
import lxml.html
from common import download


def scrape():
    url = 'http://example.webscraping.com/places/default/view/United-Kindom-239'
    html = download(url)
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
    area = td.text_content()
    return area

if __name__ == '__main__':
    print scrape()