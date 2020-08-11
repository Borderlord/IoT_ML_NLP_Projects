import random
import re
import urllib
from bs4 import BeautifulSoup

b= random.randint(0,15000);
# here i am posting data to the field1
data=urllib.urlopen("https://api.thingspeak.