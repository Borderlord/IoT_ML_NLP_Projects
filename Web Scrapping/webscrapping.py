import urllib
from bs4 import BeautifulSoup

data=urllib.urlopen("https://www.timeanddate.com/worldclock/india/new-delhi");

soup=BeautifulSoup(data