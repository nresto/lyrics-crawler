import urllib2
from bs4 import BeautifulSoup
import lxml
import os

f_loc = 'd:/lyrics/'

response = urllib2.urlopen('http://mojim.com/twh106732.htm')  
html = response.read()
root = 'http://mojim.com'


soup = BeautifulSoup(html, "lxml")

hc3s = soup.find_all('span', class_="hc3")

print len(hc3s)
counter = 0

for hc in hc3s:
    links = hc.find_all('a')
    for l in links:
        print l['href']
        counter += 1
        if not os.path.exists(f_loc + l['title']):
            res = urllib2.urlopen(root + l['href'])
            content = res.read()
            full = BeautifulSoup(content, 'lxml')
            file = open(f_loc + l['title'], 'w+')
            file.write(content)
            file.close()
                                            
