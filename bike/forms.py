from django import forms

from bike.models import Bike


class BikeCreateForm(forms.ModelForm):
    field_order = ['name', 'brand', 'model', 'mileage', 'description']

    class Meta:
        model = Bike
        fields = ('name', 'brand', 'model', 'mileage', 'description')
