from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

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
def bikepart_list(request):
    current_user = request.user
    bike_parts = BikePart.objects.filter(user=current_user)
    return render(request, 'bike/bikepart_list.html', {'bike_parts': bike_parts})


@login_required
def bikepart_details(request, id):
    bike_part = get_object_or_404(BikePart, id=id)
    return render(request, 'bike/bikepart_details.html', {'bike_part': bike_part})
