from django.shortcuts import render, redirect

from cabañas.models import Cabaña

def cabañas(request):    
    cabañas_list = Cabaña.objects.all()    
    return render(request, 'cabañas/index.html', {'cabañas_list': cabañas_list})

def change_status_cabaña(request, cabaña_id):
    cabaña = Cabaña.objects.get(pk=cabaña_id)
    cabaña.status = not cabaña.status
    cabaña.save()
    return redirect('cabañas')

# Create your views here.
