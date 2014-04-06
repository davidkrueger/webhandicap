from django.http import HttpResponse, HttpResponseRedirect
from pollango.poll import models
import bforms
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from google.appengine.ext import db
import datetime
from django.contrib.auth.decorators import login_required

import urllib2
import re
import datetime

import views

RED = 12
GREEN = 10
DEFAULT = 15

month_to_int = {
    'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Nov':11,
    'Dec':12
}


class Symbol:
    def __init__(self, symbol):
       self.symbol = symbol
       self.price = None
       self.change = None



    def __unicode__(self):
       return self.symbol + "\t" + self.price + "\t" + self.change
    def __str__(self):
       return self.symbol + "\t" + self.price + "\t" + self.change + "\t" + str(self.date)
#def parse_date(date_str, date_today):
#       fields = re.split(' +', date_str)
#       if len(fields) == 1: 
#           return date_today
#       else:
#           return datetime.datetime(2011, month_to_int[fields[0]], int(fields[1]))

def parse_date(date_str):       
        fields = re.split(' +', date_str)
        if len(fields) == 1:
            today = datetime.datetime.today()
            return datetime.datetime(today.year, today.month, today.day)
        else:
            today = datetime.datetime.today()
            return datetime.datetime(today.year, month_to_int[fields[0]], int(fields[1]))

def get_price(symbol):
    page = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=cl' % (symbol))
    text = page.read()
    #print text
    s = models.symbol()
    fields = re.split(',', text)
    

    s.symbol = symbol
    date_field = re.split(" - ", fields[1])[0][1:]
    #print "datefields"
    #print date_field
    today = datetime.datetime.today() - datetime.timedelta(hours=8)
    date_today = datetime.datetime(today.year, today.month, today.day)
    s.date = parse_date(date_field)
    s.change = re.split(' - ', fields[0])[1][:-1]

    if s.date < date_today:
           s.status = "notupdated"
    elif float(s.change[:-1])  < 0:
        s.status = "losing"
    elif s.change == "N/A":
        s.status = "notupdated"
    else:
        s.status = "winning"
    s.price = re.search("<b>.*</b>", fields[1]).group(0)[3:-4]
  #  s.price = str(date_today)
 #   s.change = str(s.date)
#    s.symbol = date_field
    #print s.date
    return s
    
def run(request):
    quote_list = []
    quote_list.append(get_price('EXWAX'))
    quote_list.append(get_price('PRWCX'))
    quote_list.append(get_price('QQQ'))
    quote_list.append(get_price('INFA'))
    quote_list.append(get_price('^GSPC'))
    quote_list.append(get_price('^VIX'))
    
    return views.render('stock_quotes.html', request, {'quotes':quote_list})
    


   
def save_new_word(word, definition):
    w = models.vocab_word()
    w.word = word
    w.definition = definition
    w.save()