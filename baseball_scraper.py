from bs4 import BeautifulSoup as bsoup
import urllib2 as url
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dum = []
h = []
k = []
y = []

quote_page = 'https://www.baseball-reference.com/leagues/MLB/bat.shtml'
page = url.urlopen(quote_page)
soup = bsoup(page,'html.parser')

for row in soup.findAll('table')[0].findAll('tbody'):
    dum = row.findAll('td',{"data-stat":"HR"})
    for i in range(len(dum)):
        hr = dum[i].text
        h.append(float(hr))

for row in soup.findAll('table')[0].findAll('tbody'):
    dum = row.findAll('td',{"data-stat":"SO"})
    for i in range(len(dum)):
        kk = dum[i].text
        k.append(float(kk))

for row in soup.findAll('table')[0].findAll('tbody'):
    dum = row.findAll('th',{"scope":"row"})
    for i in range(len(dum)):
        yr = dum[i].text
        y.append(float(yr))


slope, intercept, r_value, p_value, std_err = stats.linregress(h,k)
this = intercept + slope*np.array(h);
print intercept, slope
print r_value**2


plt.figure(1)
plt.subplot(211)
plt.scatter(h,k)
plt.plot(h, this, 'r', label='fitted line')
plt.legend()
plt.xlabel('avg hr rate')
plt.ylabel('avg so rate')

plt.subplot(212)
plt.plot(y,h,c='r',label='hr/game')
plt.plot(y,k,c='b',label='so/game')
plt.xlabel('Year')
plt.ylabel('Rate')
plt.legend()
plt.xlim(1910,2017)
plt.show()

print "done"
