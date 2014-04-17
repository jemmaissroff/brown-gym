#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import models
from google.appengine.ext.webapp import template
from google.appengine.api import images
# from google.appengine.ext import db

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        running = self.request.get('running')
        if running == "true" or running == "shaking":
         	runner = models.Running(running="True")
        	runner.put()
        	self.response.write("Just received a true get!")
        elif running == "false" or running == "still":
        	runner = models.Running(running="False")
        	runner.put()
        	self.response.write("Just received a false get!")
        else:
            run_db = models.Running.all()
            run_db.order('-time')
            html_txt = """
            <html> 
                <body>
                    There is %s someone using the treadmill
                    <p style="text-align:center">
                        <img title="logo"  src="in_use.jpg" />
                            hi ther 
                        </img>
                    </p> 
                </body>
            </html>"""
            for r in run_db.run(limit=1):
                if(r.running == "True"):
                    self.response.write(html_txt % "")
                elif(r.running == "False"):
                    self.response.write(html_txt % "not")
                else:
                    self.response.write("uh oh. not true or false")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/img', Image)
], debug=True)
