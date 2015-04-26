import re
import requests
import logging
import responder

class DefaultParser(object):

    """
    TARS string expression
    """
    find_tars = re.compile(r'(.*)TARS(.*)', re.I|re.M)

    """
    Store bot_id and room name on creation, instantiate Postman responder.
    """
    def __init__(self, bot_id, room):
        self.bot_id = bot_id
        self.room = room

        self.postman = responder.Postman(self.bot_id)

    def parse(self, request):

        """
        Check incoming message mentions TARS (!case_sensitive)
        """
        command = self.find_tars.search(request["text"])

        if command:
            """
            Simple Hello TARS reply (Hello <name>)
            """
            message_head = re.search(r'^(hello).*', command.group(1), re.I)
            if re.search(r'^(hello).*', command.group(1), re.I):
                reply = "Hello " + request["name"]

                self.postman.reply(message=reply)
