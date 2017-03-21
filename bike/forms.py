from django import forms

from bike.models import Bike, BikePart


class BikeCreateForm(forms.ModelForm):
    field_order = ['name', 'brand', 'model', 'mileage', 'description']

    class Meta:
        model = Bike
        fields = ('name', 'brand', 'model', 'mileage', 'description')


class BikepartCreateForm(forms.ModelForm):
    field_order = ['name', 'type', 'brand', 'model', 'mileage', 'bike_mounted',
                   'mount_date', 'last_service_date', 'description']

    class Meta:
        model = BikePart
        fields = ('name', 'type', 'brand', 'model', 'mileage', 'bike_mounted',
                  'mount_date', 'last_service_date', 'description')

    def __init__(self, user, *args, **kwargs):
        super(BikepartCreateForm, self).__init__(*args, **kwargs)
        self.fields['bike_mounted'] = forms.ModelChoiceField(queryset=Bike.objects.filter(user=user))
