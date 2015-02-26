# -*- coding: utf8 -*-
#!/usr/bin/env python


import webapp2
import re, string, json

# Imports for twitter
import sys
import oauth

class OAuthTwitterHandler(webapp2.RequestHandler):
    def get(self):
        action = self.request.get("action", default_value="request_token")
        
        consumer_key = self.request.get("consumer_key", default_value="")
        consumer_secret = self.request.get("consumer_secret", default_value="")
        access_token = self.request.get("access_token", default_value="")
        secret_token = self.request.get("secret_token", default_value="")
                
#        consumer_key = '7pBOCbidtVpQfTpPpwvQBL31o'
#        consumer_secret = '0M3o2TTQQQi4fqXx03XRkfUIOXZBa3sIN0w5q7culXPnVv3enb'
#        access_token = "249717000-nG3UUpnfHkhIkyhnA8KpClgVKK0Uc2kl33qTrBdP"
#        secret_token ="erdkRUxv9eKGjfNHSkpzxi0kUYGAlOvI7ESOdPuxEv4OA"

        client = oauth.TwitterClient(consumer_key, consumer_secret, "oob")
        if action == "request_token":
            respuesta = client.make_request(
                "https://api.twitter.com/1.1/statuses/home_timeline.json",
                token=access_token, secret=secret_token, protected=True)
            print("prueba")
            data = json.loads(respuesta.content)
            print(data)
            self.response.write(json.dumps(data))
            
app = webapp2.WSGIApplication([
(r'/oauth/twitter', OAuthTwitterHandler)
], debug=True)
