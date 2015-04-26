import requests
import logging
import parser

from tornado import web
from tornado.escape import json_decode


"""
Default/fallback handler
"""
class MainHandler(web.RequestHandler):
    # message = self.get_body_argument("name")

    bot_id = "3b3c7124541153d195a7c36b58"           # bot id for GroupMe API
    room = "main"                                   # Room name for filtering

    """
    Instantiate parser with id and room name
    """
    parser = parser.DefaultParser(bot_id=bot_id, room=room)

    def get(self):
        """
        Friendly message for browser requests.
        """
        self.write("Get out!")

    """
    Action to take for POST request (as with GroupMe requests)
    """
    def post(self):

        """
        Parse request body into Python dictionary.
        """
        request = json_decode(self.request.body)

        """
        Conditional to prevent replying to any bot/GroupMe action.
        """
        if request["sender_type"] == "user":
            """
            Send to parser to process.
            """
            self.parser.parse(request)



"""
Handler for requests receieved at /PS4/
"""
class PS4Handler(web.RequestHandler):

    bot_id = "6e617730812cdada18295db1a7"

    response = {"bot_id" : bot_id, "text" : "Hello PS4 users!"}

    def post(self):

        """
        Parse request body into Python dictionary.
        """
        request = json_decode(self.request.body)

        """
        Conditional to prevent replying to self
        """
        if request["sender_type"] == "user":

            requests.post("https://api.groupme.com/v3/bots/post", params=self.response)

"""
Handler for requests received at /PC/
"""
class PCHandler(web.RequestHandler):

    bot_id = "28f9f4aa21d19de60f2092cab9"

    response = {"bot_id" : bot_id, "text" : "Hello PC users!"}

    def post(self):
        """
        Parse request body into Python dictionary.
        """
        request = json_decode(self.request.body)

        """
        Conditional to prevent replying to self
        """
        if request["sender_type"] == "user":
            requests.post("https://api.groupme.com/v3/bots/post", params=self.response)
