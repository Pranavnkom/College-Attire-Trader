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
    if self.request.get("deposit_btn") == "Deposit":


class CreationPage(webapp2.RequestHandler):
    def get(self):
        creation_template = \
                jinja_current_directory.get_template('templates/creation.html')
        self.response.write(creation_template.render())

    def post(self):
        if self.request.get("create_btn") == "Submit":
            account = Accounts(email = "email", password = "password", mailing_address = "mailing_address", first_name = "first_name", last_name = "last_name")
            account.put()
            self.redirect('/')
        else:
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/creation', CreationPage)

], debug=True)
