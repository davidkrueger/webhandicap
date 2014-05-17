from django import forms
import models
import datetime
from google.appengine.ext.db import djangoforms
from google.appengine.ext import db
from google.appengine.api import users
import views
class addCourseForm(djangoforms.ModelForm):
    class Meta:
        model = models.course
        #exclude = ['created_by'] #use this to prevent a field for certain values
        exclude = ['hole_par_list']

class addScoreForm(djangoforms.ModelForm):
    class Meta:                    
        model = models.score          
        #fields = ['gross_score', 'course', 'date', 'hole1', 'hole2', 'hole3', 'hole4', 'hole5', 'hole6', 'hole7', 'hole8', 'hole9', 'hole10', 'hole11', 'hole12', 'hole13', 'hole14', 'hole15', 'hole16', 'hole17', 'hole18']
        fields = ['gross_score', 'course', 'date', 'fairways_hit', 'greens_hit', 'putts']
        #exclude = ['user', 'net_score', 'rating', 'slope', 'par', 'handicap_diff'] #use this to prevent a field for certain values
        
#form to calculate course handicap
class courseHandicapForm(djangoforms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = users.get_current_user()
        index = views.calculate_handicap_from_user(user)
        super(courseHandicapForm, self).__init__(*args, **kwargs)
        choices = [(c.slope, c.name + '--' + c.tees) for c in models.course.all()]

        self.fields['Index'] = forms.CharField(initial=index)
        self.fields['Course'] = forms.ChoiceField(choices=choices)
        self.fields['Slope'] = forms.CharField()