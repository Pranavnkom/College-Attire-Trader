import webapp2
import jinja2
import os
from models import Accounts, Products

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

current_account = {}

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = \
                jinja_current_directory.get_template('templates/login.html')
        self.response.write(login_template.render())

    def post(self):
        email = self.request.get("email")
        password =  self.request.get("password")
        if self.request.get("login_btn") == "Login":
            self.redirect('/welcome?current_user=' + email)
        else:
            self.redirect('/creation')

class CreationPage(webapp2.RequestHandler):
    def get(self):
        creation_template = \
                jinja_current_directory.get_template('templates/creation.html')
        self.response.write(creation_template.render())

    def post(self):
        pass
        # if self.request.get("create_btn") == "Submit":
        #     email = self.request.get("email")
        #     password =  self.request.get("password")
        #     mailing_address = self.request.get("mailing_address")
        #     first_name =  self.request.get("first_name")
        #     last_name =  self.request.get("last_name")
        #     account = Accounts(email = email, password = password, mailing_address = mailing_address, first_name = first_name, last_name = last_name)
        #     account.put()
        #     self.redirect('/')
        # else:
        # self.redirect('/')

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = \
                jinja_current_directory.get_template('templates/welcome.html')
        email = self.request.get("current_user")
        logged = Accounts.query(Accounts.email == email).get()
        current_account = {"logged":logged}
        self.response.write(welcome_template.render(current_account))


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/creation', CreationPage),
    ('/welcome', WelcomePage)
], debug=True)
