# `daftbot`

`daftbot` is a WIP chatbot for use with [GroupMe][0], written in python.

It has a couple of required packages, for network operations:

* [Tornado][1] is used:
  * As a server to listen for incoming requests __from__ GroupMe
  * As an application layer to handle those requests
* [Requests][2] is used to send message requests __to__ GroupMe

[0]: https://groupme.com/
[1]: http://www.tornadoweb.org/en/stable/
[2]: http://docs.python-requests.org/en/latest/
