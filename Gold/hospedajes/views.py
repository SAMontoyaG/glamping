from django.shortcuts import render,redirect
from hospedajes.models import Hospedaje

def hospedajes(request):
    hospedajes_list = Hospedaje.objects.all()
    return render(request, 'hospedajes/index.html',{'hospedajes_list': hospedajes_list})

def change_status_hospedaje(request, hospedaje_id):
    hospedaje = Hospedaje.objects.get(pk=hospedaje_id)
    hospedaje.status = not hospedaje.status
    hospedaje.save()
    return redirect('hospedajes')


# Create your views here.
