import urllib
import re
from bs4 import BeautifulSoup

#data=urllib.urlopen("https://api.thingspeak.com/update?api_key=EDLC8KHZZ4EV4KKZ&field1="+str(900));
#print data;


datafromwebsite=urllib.urlopen("https://api.thingspeak.com/channels/289288