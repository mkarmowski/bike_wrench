from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView

from bike.forms import BikeCreateForm
from bike.models import Bike, BikePart


@login_required
def bike_list(request):
    current_user = request.user
    bikes = Bike.objects.filter(user=current_user)
    return render(request, 'bike/bike_list.html', {'bikes': bikes})


@login_required
def bike_details(request, id):
    bike = get_object_or_404(Bike, id=id)
    bike_parts = BikePart.objects.filter(bike_mounted=bike)
    return render(request, 'bike/bike_details.html', {'bike': bike,
                                                      'bike_parts': bike_parts})


@login_required
def bike_create(request):
    if request.method == 'POST':
        bike_create_form = BikeCreateForm(request.POST)
        if bike_create_form.is_valid():
            new_bike = bike_create_form.save(commit=False)
            new_bike.user = request.user
            new_bike.save()
            return render(request, 'bike/bike_create_done.html')
    else:
        bike_create_form = BikeCreateForm()
    return render(request, 'bike/create.html', {'bike_form': bike_create_form})


class BikeDelete(DeleteView):
    model = Bike
    template_name = 'bike/bike_confirm_delete.html'
    success_url = reverse_lazy('bike:bike_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BikeDelete, self).dispatch(*args, **kwargs)


class BikeUpdate(UpdateView):
    model = Bike
    fields = ['name', 'brand', 'model', 'mileage', 'description']
    template_name = 'bike/bike_update.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BikeUpdate, self).dispatch(*args, **kwargs)


@login_required
def bikepart_list(request):
    current_user = request.user
    bike_parts = BikePart.objects.filter(user=current_user)
    return render(request, 'bike/bikepart_list.html', {'bike_parts': bike_parts})


@login_required
def bikepart_details(request, id):
    bike_part = get_object_or_404(BikePart, id=id)
    return render(request, 'bike/bikepart_details.html', {'bike_part': bike_part})
