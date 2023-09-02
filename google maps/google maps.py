import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyBuUF2LTfdHTmbxmoVRRnYYFlyR-jCCgyQ')

# Geocoding an address
geocode_result = gmaps.geocode('NSIT Dwarka Sect