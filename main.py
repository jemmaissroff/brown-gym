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
import urllib
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
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
                        <img title="logo"  src=%r />
                        </img>
                    </p> 
                </body>
            </html>"""
            for r in run_db.run(limit=1):
                if(r.running == "True"):
                    self.response.write(html_txt % ("",
                        "/serve/AMIfv96q4lsf7RIZPVtoH6P-dDqzLG_7yF0agkecoKKc4gwZYctt6EQ199ffN0HBJ5aIe6CHIsV9uoKXD_MOyo9OeZF3Krqd4jcT_p7xevqxooKIJPxxZJ53PN7Ppmd-9PJzoMb_WXPWd5jlWFxodXMP46UVMa-tmA"))
                elif(r.running == "False"):
                    self.response.write(html_txt % ("not",
                        "serve/AMIfv94lTNQ7v8_IjtZ897dL-xAIu1tACMFZtGL3A2zWjO2xsRn-HsB8UnvIB-aOEbpqJH6k7S1nLaLRBuh1YJutURcxziJM9-awgjGaWpQSFIsH_zQN6xwJ_6mlSbQa0wcVCBhgk94eKpe2OmkxmuqnBJvw78EOMQ"))
                else:
                    self.response.write("uh oh. not true or false")

class UploadForm(webapp2.RequestHandler):
  def get(self):
    upload_url = blobstore.create_upload_url('/ready-for-upload')
    self.response.out.write('<html><body>')
    self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
    self.response.out.write("""Upload File: <input type="file" name="file"><br> <input type="submit"
        name="submit" value="Submit"> </form></body></html>""")


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    self.redirect('/serve/%s' % blob_info.key())


class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource):
    resource = str(urllib.unquote(resource))
    blob_info = blobstore.BlobInfo.get(resource)
    self.send_blob(blob_info)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/upload', UploadForm),
    ('/ready-for-upload', UploadHandler),
    ('/serve/([^/]+)?', ServeHandler)
], debug=True)
