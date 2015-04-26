import re
import requests
import logging

class DefaultParser(object):

    find_tars = re.compile(r'(.*)TARS(.*)', re.I|re.M)

    def __init__(self, bot_id, room):
        self.bot_id = bot_id
        self.room = room

    def parse(self, request):

        command = self.find_tars.search(request["text"])

        if command:
            message_head = re.search(r'^(hello).*', command.group(1), re.I)
            if re.search(r'^(hello).*', command.group(1), re.I):
                reply = "Hello " + request["name"]

            self.response = {"bot_id": self.bot_id, "text": reply}

            requests.post("https://api.groupme.com/v3/bots/post", params=self.response)
