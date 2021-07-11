from django.forms import ModelForm
from .models import survey, Page1, Page2, Page3, Page4, Page5
from django import forms


class SurveyForm(ModelForm):
    class Meta:
        model = survey
        fields = '__all__'


class Page1Form(ModelForm):
    class Meta:
        model = Page1
        fields = ['p1q1', 'p1q2', 'p1q3', 'p1q4','anno']
        widgets = {
            'p1q1': forms.RadioSelect(),

        }

class Page2Form(ModelForm):
    class Meta:
        model = Page2
        fields = ['p2q1', 'p2q2', 'p2q3', 'p2q4']
        widgets = {
            'p2q1': forms.RadioSelect(),

        }

class Page3Form(ModelForm):
    class Meta:
        model = Page3
        fields = ['p3q1', 'p3q2', 'p3q3', 'p3q4']
        widgets = {
            'p3q1': forms.RadioSelect(),

        }

class Page4Form(ModelForm):
    class Meta:
        model = Page4
        fields = ['p4q1', 'p4q2', 'p4q3', 'p4q4']
        widgets = {
            'p4q1': forms.RadioSelect(),

        }

class Page5Form(ModelForm):
    class Meta:
        model = Page5
        fields = ['p5q1', 'p5q2', 'p5q3', 'p5q4']
        widgets = {
            'p5q1': forms.RadioSelect(),

        }