from google.appengine.ext import ndb

class Accounts(ndb.Model):
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    mailing_address = ndb.StringProperty(required=True)
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    tokens = ndb.StringProperty(required=True)


class Products(ndb.Model):
    college = ndb.StringProperty(required=True)
    size = ndb.StringProperty(required=True)
    color = ndb.StringProperty(required=True)
    is_counter = ndb.BooleanProperty(required=True)
    neck_type = ndb.StringProperty(required=True)
    sleeve_type = ndb.StringProperty(required=True)
    picture = ndb.StringProperty(required=True)
    #description = ndb.StringProperty(required=True)
