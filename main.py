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
from google.appengine.ext import db

class MainHandler(webapp2.RequestHandler):

    def get(self):
		#request = Request.blank('/test?check=a&check=b&name=Bob')


        self.post()

		# get_values = request.GET
		# self.response.write(get_values)
		# self.response.write(name)
    def post(self):
        running = self.request.get('running')
        if running == "true":
         	runner = models.Running(running="True")
        	runner.put()
        	self.response.write("Just received a true get!")
        elif running == "false":
        	runner = models.Running(running="False")
        	runner.put()
        	self.response.write("Just received a false get!")
        else:

            run_db = models.Running.all()
            run_db.order('-time')
            for r in run_db.run(limit=1):
                if(r.running == "True"):
                    self.response.write("The treadmill is currently occupied.")
                elif(r.running == "False"):
                    self.response.write("The treadmill is not currently occupied.")
                else:
                    self.response.write("uh oh. not true or false")


#run = db.GqlQuery("SELECT * FROM RUNNING")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
