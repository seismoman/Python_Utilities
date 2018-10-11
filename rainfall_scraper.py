from bs4 import BeautifulSoup as bsoup
import urllib2 as url
import numpy as np
import matplotlib.pyplot as plt

quote_page = 'http://www.laalmanac.com/weather/we08aa.php'
page = url.urlopen(quote_page)
soup = bsoup(page,'html.parser')

net = []
std = []
high = []

for row in soup.findAll('table')[0].findAll('tbody'):
    for i in range((len(row)-1)/2):
        tmp = []
        ind = i*14
        year = row.findAll('td')[0+ind].text
        jul = row.findAll('td')[1+ind].text
        aug = row.findAll('td')[2+ind].text
        sep = row.findAll('td')[3+ind].text
        tob = row.findAll('td')[4+ind].text
        nov = row.findAll('td')[5+ind].text
        dec = row.findAll('td')[6+ind].text
        jan = row.findAll('td')[7+ind].text
        feb = row.findAll('td')[8+ind].text
        mar = row.findAll('td')[9+ind].text
        apr = row.findAll('td')[10+ind].text
        may = row.findAll('td')[11+ind].text
        jun = row.findAll('td')[12+ind].text
        tot = row.findAll('td')[13+ind].text
        if tot == '---':
            tot = 0
        net.append(float(tot))
        agg = np.array((jul,aug,sep,tob,nov,dec,jan,feb,mar,apr,may,jun))
        for i in range(len(agg)):
            if isinstance(agg[i],int)==True:
                tmp.append(float(agg[i]))
        std.append(np.std(tmp))
        high.append(max(tmp))
        del(tmp)

b = np.array(net)
y = b[2:][::-1] #reverses order of array
x = np.arange(1877,2017)

c = np.array(std)
z = c[2:][::-1]

d = np.array(high)
w = d[2:][::-1]

cm = plt.cm.get_cmap('RdYlBu')

plt.figure()
sc = plt.scatter(x, y, marker='o', s=50, c=w, cmap=cm)
plt.colorbar(sc, shrink=0.5)
plt.plot(x,y)
plt.errorbar(x, y, marker=None, fmt=None, yerr=z, ecolor='g')
plt.title('Total Rainfall in Los Angeles per Year')
plt.ylabel('Rainfall (in)')
plt.xlabel('Year')
plt.xticks(np.arange(1880,2020,10))
plt.xlim(1876,2017)
#plt.savefig('test.png', bbox_inches='tight')
plt.show()
