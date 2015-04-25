import requests
import logging

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

requests.post("http://127.0.0.1:5000/", params=something)
logging.warning("root")
requests.post("http://127.0.0.1:5000/PS4/", params=something)
logging.warning("PS4")
requests.post("http://127.0.0.1:5000/PC/", params=something)
logging.warning("PC")
