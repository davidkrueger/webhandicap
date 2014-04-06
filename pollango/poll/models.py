from google.appengine.ext import db
from django import forms


class course(db.Model):
    name = db.StringProperty()
    tees = db.StringProperty()
    yardage = db.IntegerProperty()
    par = db.IntegerProperty()
    slope = db.IntegerProperty()
    rating = db.FloatProperty()
    #hole_handicap_list = db.ListProperty(int)
    #hole_yardage_list = db.ListProperty(int)
    hole_par_list = db.ListProperty(int)
    def __unicode__(self):
        return '%s--%s' % (self.name,  self.tees)
        
class score(db.Model):
    user = db.UserProperty()
    gross_score = db.IntegerProperty()
    net_score = db.IntegerProperty()
    course = db.ReferenceProperty(course)
    par = db.IntegerProperty()
    slope = db.IntegerProperty()
    rating = db.FloatProperty()
    date = db.DateProperty()
    handicap_diff = db.FloatProperty()
    hole_score_list = db.ListProperty(int)  #might not need this
    greens_hit = db.IntegerProperty()
    fairways_hit = db.IntegerProperty()
    putts = db.IntegerProperty()
    
    
class symbol(db.Model):
    symbol = db.StringProperty()
    price = db.StringProperty()
    change = db.StringProperty()
    
class vocab_word(db.Model):
    word = db.StringProperty()
    definition = db.StringProperty()
    
    def __unicode__(self):
        return '%s--%d' % (self.course.name,  self.gross_score)

