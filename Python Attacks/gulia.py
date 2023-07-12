from robobrowser import RoboBrowser
from time import sleep
import random
 
#i=0

#sleep(1)
browser = RoboBrowser(parser='html.parser')
browser.open('http://cyberkeys.us/contact')
#print (random.randint(1,12301983013801932801239))
# Get the signup form
cform = browser.get_form(action='/contact/#wpcf