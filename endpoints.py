import geoip2.database
import json

with open("config.json") as fp:
	config = json.load(fp)

reader = geoip2.database.Reader("database.mmdb")

endpoints = {}

def getInfos(ip):
	try:
		tmp = reader.city(ip)
		return {
			"success":True,
			"cityName":tmp.city.name,
			"cityNames":tmp.city.names,
			"countryCode":tmp.country.iso_code,
			"countryName":tmp.country.name,
			"countryNames":tmp.country.names,
			"postalCode":tmp.postal.code,
			"RegionCode":tmp.subdivisions.most_specific.iso_code,
			"RegionName":tmp.subdivisions.most_specific.name,
			"RegionNames":tmp.subdivisions.most_specific.names,
			"location":{
				"lat":tmp.location.latitude,
				"lon":tmp.location.longitude
			}
		}
	except Exception as e:
		return {"success":False, "error":str(e)}

def jsonE(request):
	ip = request.path[6:]
	request.send_response(200)
	request.send_header('Content-type','application/json; charset=utf-8')
	request.end_headers()

	request.wfile.write(bytes(json.dumps(getInfos(ip)), "utf8"))

endpoints["/json/"] = jsonE