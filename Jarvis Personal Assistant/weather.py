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

html_str="""
<html>
<table>
<tr>
<td>
&nbsp;&nbsp;&nbsp;
</td>
<td>
&nbsp;
<div id="openweathermap-widget-15"></div>
<script>window.myWidgetPara