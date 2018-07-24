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
    counter = ndb.StringProperty()
    neck_type = ndb.StringProperty(required=True)
    sleeve_type = ndb.StringProperty(required=True)
    picture = ndb.BlobProperty(required=True)
    tokens = ndb.StringProperty(required=True)
    id = ndb.StringProperty(required=True)

class Wish(ndb.Model):
    college = ndb.StringProperty(required=True)
    size = ndb.StringProperty(required=True)
    tokens = ndb.StringProperty(required=True)
    id = ndb.StringProperty(required=True)
