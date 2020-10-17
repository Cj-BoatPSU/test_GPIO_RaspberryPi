import Adafruit_DHT as adht
from . import Beaglebone_Black
platform = get_platform()
humidity,temperature = adht.read_retry(adht.DHT22, 4, platform) 
print( 'humidity: {1:0.1f} and temperature: {1:0.1f} C'.format(humidity, temperature)) 