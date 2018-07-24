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

def get_products():
    logs = Products.query().fetch()
    dic = {'logs': logs}
    return dic

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
    def post(self):
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.tokens == token).get()
        current_account = {"logged":logged}
        if self.request.get("upload_btn") == "upload":
            self.redirect("/upload?current_user=" + logged.tokens)
        if self.request.get("status_btn") == "status":
            self.redirect("/status?current_user=" + logged.tokens)
        if self.request.get("market_btn") == "marketplace":
            self.redirect("/marketplace?current_user=" + logged.tokens)

class UploadPage(webapp2.RequestHandler):
    def get(self):
        upload_template = \
                jinja_current_directory.get_template('templates/upload.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.tokens == token).get()
        current_account = {"logged":logged}
        self.response.write(upload_template.render(current_account))

    def post(self):
        college = self.request.get("college")
        size = self.request.get("size")
        color = self.request.get("color")
        is_counter = False
        neck_type = self.request.get("neck_type")
        sleeve_type = self.request.get("sleeve_type")
        picture = self.request.get("image")
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.tokens == token).get()
        current_account = {"logged":logged}
        product = Products(college = college, size = size, color = color, is_counter = is_counter, neck_type = neck_type, sleeve_type = sleeve_type, picture = picture, tokens = token)
        product.put()
        self.redirect("/welcome?current_user=" + logged.tokens)

class MarketPage(webapp2.RequestHandler):
    def get(self):
        market_template = \
                jinja_current_directory.get_template('templates/marketplace.html')
        self.response.write(market_template.render(get_products()))

class StatusPage(webapp2.RequestHandler):
    def get(self):
        status_template = \
                jinja_current_directory.get_template('templates/status.html')
        token = self.request.get("current_user")
        logged = Accounts.query(Accounts.tokens == token).get()
        current_account = {"logged":logged}
        self.response.write(status_template.render(current_account))



app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/creation', CreationPage),
    ('/welcome', WelcomePage),
    ('/upload', UploadPage),
    ('/status', StatusPage),
    ('/marketplace', MarketPage)
], debug=True)
