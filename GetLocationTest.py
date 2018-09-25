import geolocation
from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient as gDist
from Properties import geoKey
import logging
logging.basicConfig(filename="GetLocationTest.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

addressOne = "1600 Pennsylvania Ave NW, Washington, DC"
addressTwo = "350 5th Ave, New York, NY"
addresses = [{"address":addressOne},{"address":addressTwo}]

maps = GoogleMaps(api_key=geoKey)

def getMapsLocation(address):
	location = maps.search(location=address)

	logging.debug(f"All returned location from Google Maps Search for {address}:\t{location.all()}") # returns a "LocationModel" object
	print(location.all())

	my_location = location.first() # returns only first location which should be the correct one

	logging.info(f"Google Maps Search for {address} resulted in: {my_location}")
	logging.debug(f"my_location.city: {my_location.city}, my_location.route: {my_location.route}, my_location.street_number: {my_location.street_number}, my_location.postal_code: {my_location.postal_code}, my_location.lat: {my_location.lat}, my_location.lng: {my_location.lng}")

for address in addresses:
	location = getMapsLocation(address["address"])
	address["location"] = location
	i = addresses.index(address) + 1
	logging.info(f"Data for address{i}: {address}")