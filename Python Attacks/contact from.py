
from robobrowser import RoboBrowser

browser = RoboBrowser(parser='html.parser')
browser.open('http://www.battleramp.com/contact.htm')

# Get the signup form