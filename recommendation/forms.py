from django import forms

class RecommendationForm(forms.Form):
    npk1 = forms.CharField(label='Nitrogen', max_length=100)
    npk2 = forms.CharField(label='Phosphorous', max_length=100)
    npk3 = forms.CharField(label='Potassium', max_length=100)
    rainfall = forms.CharField(label='Rainfall', max_length=100)
    temperature = forms.CharField(label='Temperature', max_length=100)
    humidity = forms.CharField(label='Humidity', max_length=100)
    soil_ph = forms.CharField(label='Soil pH', max_length=100)

