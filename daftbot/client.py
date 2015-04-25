import tornado.ioloop
import tornado.web
import tornado.options
import os
import handler

"""
Application class used to instantiate the application by daftbot
__init__.
"""
class Application(object):

    """
    Route incoming POST request to handler according to room
    received from (different rooms post to different URLS).
    TODO: Iterate through env dictionary.
    """
    application = tornado.web.Application([
        (r"/", handler.MainHandler),
        (r"/PS4/", handler.PS4Handler),
        (r"/PC/", handler.PCHandler),
    ])


    def __init__(self):
        """
        Set port to listen on (via env var, defaults to 5000) ad
        start IOLoop
        """
        tornado.options.parse_command_line()
        self.application.listen((os.environ.get("PORT", 5000)))
        tornado.ioloop.IOLoop.instance().start()
