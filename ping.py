import requests
import logging
import json
from tornado.escape import json_encode

"""
Quick test script to check responses
"""
something = {
  "attachments": [],
  "avatar_url": "http://i.groupme.com/123456789",
  "created_at": 1302623328,
  "group_id": "1234567890",
  "id": "1234567890",
  "name": "John",
  "sender_id": "12345",
  "sender_type": "user",
  "source_guid": "GUID",
  "system": False,
  "text": "Hello world",
  "user_id": "1234567890"
}

something_json = json_encode(something)

requests.post("http://127.0.0.1:5000/", data=something_json)
logging.warning("world")

something["text"] = "Hello TARS"
something_json = json_encode(something)

requests.post("http://127.0.0.1:5000/", data=something_json)
logging.warning("hello tars")
# requests.post("http://127.0.0.1:5000/PS4/", data=something_json)
# logging.warning("PS4")
# requests.post("http://127.0.0.1:5000/PC/", data=something_json)
# logging.warning("PC")
