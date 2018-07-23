from google.appengine.ext import ndb

class Accounts(ndb.Model):
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    mailing_address = ndb.StringProperty(required=True)

class Products(ndb.Model):
    college = ndb.StringProperty(required=True)
    size = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
