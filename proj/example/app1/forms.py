from django import forms
from django.core import validators

def validate_location(value):
    print("validate_location called, value='{}'".format(value))
    if (value[0] != "r") or (not value[1].isdigit()) or \
     (value[2] != "c") or (not value[3].isdigit()):
        print("raising error!")
        raise forms.ValidationError("Use row and column format, e.g. r1c1.")

class SudokuForm(forms.Form):
    location=forms.CharField(min_length=4, max_length=4, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'r1c1','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(4),
        validators.MaxLengthValidator(4),
        validate_location])
    value = forms.CharField(min_length=1, max_length=1, strip=True,
        widget= forms.TextInput(attrs={'placeholder':'1','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1),
        validators.MaxLengthValidator(1)])
