# Airthings :dash: Tools

The scripts I collect here have been derived from several originals from the
[Airthings repositories](https://github.com/Airthings/), especially for the [WavePlus model](https://github.com/Airthings/waveplus-reader).

Improvements I attempt to make are:
* Each script should only do one thing, e.g. don't mix device discovery with extracting data from the sensors
* Handling of Bluetooth errors, e.g. don't let the script crash with a stacktrace
* Have proper parseable output (JSON)
* Use Python 3 :snake:

These are also my first attempts ever at writing something halfwhat serious in Python. If you see an opportunity for improving the code, give me a hint.

##### Modus Operandi

The intended way to use these tools is that the (yet to be written) discovery script is manually used to, well, discover the nearby devices (meaning, find the Bluetooth MAC address to a known device serial number). Then the read script is called (ideally as a cronjob) with a bunch of parameters including said MAC address, a location name (useful if more than one device is queried) and a URL that will receive the extracted data as a HTTP post request. The latter might be skipped by another parameter to then output the JSON data on the terminal, if I fancy it.

Anyway, the recipient of the data might be a web application of some sorts that will interpret the raw data and do something with it, like store it in a database, calculate time series, act on certain thresholds, anything. Since the Python read script requires root privileges to access the Bluetooth stack, this is a welcome way of splitting device querying and further processing.

The output contains the raw, uninterpreted data. The calculations into f.ex. temperature or atmospheric pressure are fairly easy. I wanted to have all raw data to store it for later processing, and there are some sensor values that are not explained in the original Airwaves scripts. Until I find out what they mean, I do not want to loose historical data, hence the eleven values in the raw data array of which seven are known sensors.

##### ToDo

* Explain data format here :closed_book:
* Further improve error handling :boom:
* Implement HTTP post of JSON data :outbox_tray:
* Make a device discovery script :mag:
* Maybe find out what these other sensor values are :thinking:

<hr/>

&copy; 2018 [Airthings AS](https://www.airthings.com/about-us) &bull; &copy; 2021 Philipp Gröschler &bull; [MIT License](https://mit-license.org)
