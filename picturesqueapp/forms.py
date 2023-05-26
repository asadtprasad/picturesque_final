from django import forms
from django.forms import CharField
from picturesqueapp.models import pmodel



class pform(forms.Form):
	
	img = forms.FileField()
	class Meta:
		model = pmodel
		fields = ['uid','state','tags','img'] 
		

		
		
