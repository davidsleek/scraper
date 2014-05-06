import urllib2
import re
from bs4 import BeautifulSoup


url = "http://www.filmsofafrica.com/Ethiopia/Adwa.htm"
#movie_title = raw_input("please enter the movie title")
#url = url + movie_title


content = urllib2.urlopen(url).read()


soup = BeautifulSoup(content)

x = soup.table.find_all("strong")
y = soup.find_all(class_="style1")
z = soup.table.find_all("p")


output = str(x[0].get_text())
#output1 = str(x[1].get_text())
#output2 = str(x[2].get_text())
output3 = str(x[3].get_text())
output4 = str(x[4].get_text())
output5 = str(x[5].get_text())

title = str(y[1].get_text())
title1 = str(y[2].get_text())
title2 = str(y[3].get_text())
about = str(z[1].get_text())



print output 
print about
#print output1 + output2
print title + " : " + output3
print title1 + " : " + output4
print title2 + " : " + output5

