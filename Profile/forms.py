__author__ = 'moholkar.hrishikesh2'
__author__ = 'moholkar.hrishikesh2'
from django import forms

from Profile.models import Messages

class CommentForm(forms.Form):
    #class Meta:
        #model = Messages
       # fields = ('Name','body','EmailAddress')

        Name = forms.CharField()
        body = forms.CharField(max_length=5000)
        Email = forms.EmailField()
