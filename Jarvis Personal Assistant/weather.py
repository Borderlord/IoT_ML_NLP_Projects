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
<script>window.myWidgetParam ? window.myWidgetParam : window.myWidgetParam = []; 
 window.myWidgetParam.push({id: 15,cityid:
 """

html_str1="""
,appid: '341f89685387c67a16d0d9c4e3f3da97',units: 'metric',
 containerid: 'openweathermap-widget-15',  });  (function() {var script = document.createElement('script');
 script.async = true;script.charset = "utf-8";
 script.src = "https://openweathermap.org/themes/openweathermap/assets/vendor/owm/js/weather-widget-generator.js";
 var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(script, s);  })();</script>

</td>

<td>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</td>

<td>
&nbsp