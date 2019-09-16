from http.server import BaseHTTPRequestHandler, HTTPServer
import json

import endpoints

with open("config.json") as fp:
	config = json.load(fp)

class GeoIP(BaseHTTPRequestHandler):

	def do_GET(self):

		for endpoint in endpoints.endpoints.keys():
			if not self.path.find(endpoint):
				endpoints.endpoints[endpoint](self)
				return

		# Default page
		self.send_response(404)

		self.send_header('Content-type','text/plain')
		self.end_headers()

		message = """
Info :
Author : 5IGI0
Source : https://github.com/5IGI0/SelfHosted-Geoip-Api
Version : 1.0.0

EndPoints :
/json/<ip> - json ouput
"""

		self.wfile.write(bytes(message, "utf8"))
		return

server_address = ('127.0.0.1', config["port"])
httpd = HTTPServer(server_address, GeoIP)
print('running server...')
httpd.serve_forever()