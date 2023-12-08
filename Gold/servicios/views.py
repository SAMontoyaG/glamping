from django.shortcuts import render, redirect
from servicios.models import Servicio

def servicios(request):
    servicios_list = Servicio.objects.all()       
    return render(request, 'servicios/index.html', {'servicios_list': servicios_list}

)
def change_status_servicios(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    servicio.status = not servicio.status
    servicio.save()
    return redirect('servicios')
 


# Create your views here.
