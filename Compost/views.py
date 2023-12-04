from django.shortcuts import render, HttpResponse
from django.contrib import messages
from datetime import timedelta, datetime
from .models import Compost

from django.utils import timezone
def timelyUpdate(request):
    if request.method == 'POST':
        Uid_value = request.POST.get('Uid')
        Temp_value = request.POST.get('Temp')
        Humidity_value = request.POST.get('Humidity')

        Items = Compost.objects.filter(uid=uid_value)

        if Items.exists():
            for item in Items:
                item.Temp = Temp_value
                item.Humidity = Humidity_value
                your_object.save()
    return HttpResponse("Compost updated")

    
def alerts(request):
    custom_message = request.GET.get('custom_message', None)

    if custom_message:
        messages.warning(request, custom_message)
    return HttpResponse("Alert Recieved")


def home(request):
    registered_username = request.session.get('registered_username')
    Items = Compost.objects.filter(Uid=registered_username)
    return render(request, 'home.html', {'registered_username': registered_username,'Items':Items})


from .forms import TemperatureHumidityForm
def add_compost(request):
    if request.method == 'POST':
        registered_username = request.session.get('registered_username')
        Uid_value = registered_username
        Temp_value = request.POST.get('Temp')
        Humidity_value = request.POST.get('Humidity')
        Date_of_add_value = timezone.now()

        record = Compost.objects.create(
            Uid=Uid_value,
            Temp=Temp_value,
            Humidity=Humidity_value,
            Date_of_add=Date_of_add_value
        )
    return HttpResponse("dATA Recieved")
    