import tornado.ioloop
import tornado.web
import os
from guyman import handler


class Application(object):

	"""
	Route incoming POST request to handler according to room
	received from (different rooms post to different URLS)
	"""
	application = tornado.web.Application([
		(r"/", handler.MainHandler),
		(r"/PS4/", handler.PS4Handler),
		(r"/PC/", handler.PCHandler),
	])


	def __init__(self):
		self.application.listen((os.environ.get("PORT", 5000)))
		tornado.ioloop.IOLoop.instance().start()
