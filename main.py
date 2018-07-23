import webapp2
import jinja2
import os
from models import Accounts, Products

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = \
                jinja_current_directory.get_template('templates/login.html')
        self.response.write(login_template.render())

    def post(self):
        username = self.request.get("username")
        password =  self.request.get("password")
        




app = webapp2.WSGIApplication([
    ('/', LoginPage),

], debug=True)
