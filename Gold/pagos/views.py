from django.shortcuts import render, redirect

from pagos.models import Pago

def pagos(request):    
    pagos_list = Pago.objects.all()    
    return render(request, 'pagos/index.html', {'pagos_list': pagos_list})

def change_status_pago(request, pagos_id):
    pagos = Pago.objects.get(pk=pagos_id)
    pagos.status = not pagos.status
    pagos.save()
    return redirect('pagos')
# Create your views here.
