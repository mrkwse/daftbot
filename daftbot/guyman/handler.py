import requests

from tornado import web



class MainHandler(web.RequestHandler):

	bot_id = "3b3c7124541153d195a7c36b58"

	response = {"bot_id" : bot_id, "text" : "Hello robots!"}

	def post(self):
		requests.post("https://api.groupme.com/v3/bots/post", params=self.response)


class PS4Handler(web.RequestHandler):

	bot_id = "6e617730812cdada18295db1a7"

	response = {"bot_id" : bot_id, "text" : "Hello PS4 users!"}

	def post(self):
		requests.post("https://api.groupme.com/v3/bots/post", params=self.response)


class PCHandler(web.RequestHandler):

	bot_id = "28f9f4aa21d19de60f2092cab9"

	response = {"bot_id" : bot_id, "text" : "Hello PC users!"}

	def post(self):
		requests.post("https://api.groupme.com/v3/bots/post", params=self.response)
