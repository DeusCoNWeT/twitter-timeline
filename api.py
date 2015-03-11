# -*- coding: utf8 -*-
#!/usr/bin/env python


import webapp2
import re, string, json

# Imports for twitter
import sys
import oauth

class OAuthTwitterHandler(webapp2.RequestHandler):
    def get(self):
        accion = self.request.get("accion", default_value="request_timeline")
        consumer_key = self.request.get("consumer_key", default_value="")
        consumer_secret = self.request.get("consumer_secret", default_value="")
        access_token = self.request.get("access_token", default_value="")
        secret_token = self.request.get("secret_token", default_value="")
        count = self.request.get("count", default_value="20")
        since_id = self.request.get("since_id", default_value="")

        client = oauth.TwitterClient(consumer_key, consumer_secret, "oob")

        if(accion == "request_timeline"):
            respuesta = client.make_request(
                "https://api.twitter.com/1.1/statuses/home_timeline.json",
                token=access_token, secret=secret_token,additional_params={"count": count}, protected=True)
            self.response.write(respuesta.content)
        elif(accion == "refrescar"):
            respuesta = client.make_request(
                "https://api.twitter.com/1.1/statuses/home_timeline.json",
                token=access_token, secret=secret_token,additional_params={"since_id": since_id}, protected=True)
            self.response.write(respuesta.content)

app = webapp2.WSGIApplication([
        (r'/oauth/twitter', OAuthTwitterHandler)
], debug=True)
