import requests

r = requests.get('http://httpbin.org/status/418')

class Teapot(Object):

	def __init__(self):
		self.teapot = r.text
