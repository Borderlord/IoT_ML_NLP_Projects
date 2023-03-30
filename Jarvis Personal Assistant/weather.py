import requests
import re
import webbrowser as wb

inn = raw_input("Location :");


def textfile():
  with open("C:\Users\Vikas Yadav\Desktop\city_list.txt") as f:
   for line in f:
    if inn in line:
       pb=re.findall('\d+', line) 
       return pb; 
b=textfile()

html_s