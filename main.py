import webapp2
import jinja2
import os

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = \
                jinja_current_directory.get_template('templates/login.html')
        transactions = Transaction.query().fetch()
        self.response.write(login_template.render())
    def post(self):
                



app = webapp2.WSGIApplication([
    ('/', WelcomePage),

], debug=True)
