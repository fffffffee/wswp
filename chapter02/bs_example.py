from bs4 import BeautifulSoup
from common import download


url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
html = download(url)
soup = BeautifulSoup(html, "html5lib")
# locate the area row
tr = soup.find(attrs={'id':'places_area__row'})
td = tr.find(attrs={'class':'w2p_fw'}) #locate the area tag
area = td.text # extract the text from this tag
print area