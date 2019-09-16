# SelfHosted GeoIP API

## Setup

**Step 1 - install Python3 and pip**

linux (debian-based) :
	``sudo apt install python3 python3-pip``

**Step 2 - install geoip2 module**

linux :
	``pip3 install -U geoip2``

**Step 3 - download geolite2-city database**

linux : 
	``wget -O GeoLite2-City.tar.gz https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz``
	``tar xvzf GeoLite2-City.tar.gz``
	``cp GeoLite2-City_<number>/GeoLite2-City.mmdb database.mmdb``

**Step 4 - run and try**

linux : 
	``screen -m -d python3 main.py``
	_wait some seconds_
	``wget -qO - http://127.0.0.1:8080/json/8.8.8.8``