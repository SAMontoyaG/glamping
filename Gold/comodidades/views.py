from django.shortcuts import render, redirect
from comodidades.models import Comodidad

def comodidades(request):
    comodidades_list = Comodidad.objects.all()  
    return render(request, 'comodidades/index.html',{'comodidades_list': comodidades_list}
)
def change_status_comodidad(request, comodidades_id):
    comodidades = Comodidad.objects.get(pk=comodidades_id)
    comodidades.status = not comodidades.status
    comodidades.save()
    return redirect('comodidades')



# Create your views here.
