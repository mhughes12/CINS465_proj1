from django import forms
from django.core import validators

def validate_location(destination):
    print("validate_location called, destination='{}'".format(destination))
    if ((destination[0] != "A") or (not destination[1].isdigit()) or (destination[0] != "B") or (destination[0] != "C") or (destination[0] != "D") or (destination[0] != "E") or (destination[0] != "F") or 
    (destination[0] != "G") or (destination[0] != "H")):
        print("error!")
        raise forms.ValidationError("Use row and column format, e.g. A1 or B1.")

class chessForm(forms.Form):
    location=forms.CharField(min_length=2, max_length=2, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'A1','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(2),
        validators.MaxLengthValidator(2),
        validate_location])
    destination = forms.CharField(min_length=2, max_length=2, strip=True,
        widget= forms.TextInput(attrs={'placeholder':'B3','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(2),
        validators.MaxLengthValidator(2)])
