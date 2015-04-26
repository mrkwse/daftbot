import requests

"""
Send function transmits <payload> (containing id and message) to GroupMe
URL via POST.
"""
def send(payload):

	requests.post("https://api.groupme.com/v3/bots/post", params=payload)

class Postman(object):
	"""
	Input bot_id so replies go to correct bot/room.
	"""
	def __init__(self, bot_id):
		self.bot_id = bot_id

	"""
	Populate <payload> dictionary with id and message for transmission.
	"""
	def reply(self, message):
		self.payload = {"bot_id": self.bot_id, "text": message}
		send(payload=self.payload)
