# myapp/forms.py
from django import forms

class TemperatureHumidityForm(forms.Form):
    temperature = forms.FloatField(label='Temperature')
    humidity = forms.FloatField(label='Humidity')
