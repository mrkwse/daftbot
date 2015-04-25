import os

class Robot(object):
	def __init__(self):
		# The name the bot is to reply to in a room (from env var)
		self.bot_name = str(os.environ.get('BOT_NAME', 'TARS'))
		# The id a bot is to respond to GroupMe as (from env var)
		self.bot_id = str(os.environ.get('BOT_ID'))
