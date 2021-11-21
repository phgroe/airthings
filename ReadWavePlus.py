from bluepy.btle import UUID, Peripheral, BTLEDisconnectError
from datetime import datetime, timezone

import struct
import sys


if len (sys.argv) != 3:
	print ('USAGE: ' + sys.argv [0] + ' [location name] [mac address]')
	sys.exit (1)


locationName = sys.argv [1].lower ()
macAddr = sys.argv [2].lower ()

# TODO Parameterchecks


now = datetime.now (timezone.utc).replace (microsecond = 0)
outputStr = '{ "time": "' + now.isoformat () + 'Z", "location": "' + locationName + '"'

waveUUID = UUID ("b42e2a68-ade7-11e4-89d3-123b93f75cba")

needResult = True
noAttempts = 0
errorCount = 0

while noAttempts < 5 and needResult:

	try:
		# Connect
		peripheral = Peripheral (macAddr)
		characteristics = peripheral.getCharacteristics (uuid = waveUUID) [0]

		# Read sensors
		rawData = struct.unpack ('<BBBBHHHHHHHH', characteristics.read ())
		strData = list (map (lambda s: str (s), rawData))

		# Disconnect
		peripheral.disconnect ()
		needResult = False

		outputStr += ', "sensors": [ ' + (', '.join (strData [1:])) + ' ]'

	except BTLEDisconnectError:
		errorCount += 1

	finally:
		noAttempts += 1

outputStr += ', "errorCount": ' + str (errorCount) + ' }'

print (outputStr)
