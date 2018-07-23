import webapp2
import jinja2
import os
import string
import random
from models import Accounts, Products

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

current_account = {}

def id_generator(size=90, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = \
                jinja_current_directory.get_template('templates/login.html')
        self.response.write(login_template.render())

    def post(self):
        email = self.request.get("email")
        logged = Accounts.query(Accounts.email == email).get()
        if self.request.get("login_btn") == "Login" and logged.password == self.request.get("password"):
            self.redirect('/welcome?current_user=' + logged.tokens)
        else:
            self.redirect('/creation')

class CreationPage(webapp2.RequestHandler):
    def get(self):
        creation_template = \
                jinja_current_directory.get_template('templates/creation.html')
        self.response.write(creation_template.render())

    def post(self):

        if self.request.get("create_btn") == "Submit":
            email = self.request.get("email")
            password =  self.request.get("password")
            mailing_address = self.request.get("mailing_address")
            first_name =  self.request.get("first_name")
            last_name =  self.request.get("last_name")
            token = id_generator()
            account = Accounts(email = email, password = password, mailing_address = mailing_address, first_name = first_name, last_name = last_name, tokens = token)
            account.put()
            self.redirect('/')
        else:
            self.redirect('/')

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = \
                jinja_current_directory.get_template('templates/welcome.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.tokens == token).get()
        current_account = {"logged":logged}
        self.response.write(welcome_template.render(current_account))


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/creation', CreationPage),
    ('/welcome', WelcomePage)
], debug=True)
