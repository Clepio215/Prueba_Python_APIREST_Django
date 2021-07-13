from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import tophistorias
import requests
from django.db.models.functions import Extract
import datetime

# Create your views here.

def courses(request):
    fecha_actual=datetime.datetime.now()
    cache = tophistorias.objects.all().values('created_at')#trae el query de la fecha
    req = requests.request('GET','https://hacker-news.firebaseio.com/v0/beststories.json')
    datos = req.json()
    
    date=list(cache)
    value=date[0]
    value2=value['created_at']
    secs=fecha_actual.second
    secs_cache=value2.second
    mins=fecha_actual.minute
    mins_cache=value2.minute
    segundosactual=int(secs)
    segundos_cache=int(secs_cache)
    proxy=segundos_cache-segundosactual
    proxymins=mins_cache-mins

    if(proxy>20)or(proxy<-20)or(proxymins!=0):
        mensaje="expiro"
        data_a_eliminar=tophistorias.objects.all()
        data_a_eliminar.delete()
        objdatos = tophistorias()
        objdatos.itemid = datos
        objdatos.created_at = fecha_actual
        objdatos.save()

        
    else:
        mensaje="no expiro"
    
    return JsonResponse(mensaje, safe=False)

def ConsultDatos(request, codigo):

    #trae el query de la los top
    data_tophistorias=tophistorias.objects.all().values('itemid')
    lis2=list(data_tophistorias)
    vl=lis2[0]
    datos_list_bd=vl['itemid']
    cogido_num=int(codigo)

    for itr in range(len(datos_list_bd)):
       if(cogido_num==datos_list_bd[itr]):
        req = requests.request('GET','https://hacker-news.firebaseio.com/v0/item/'+codigo+'.json')
        datos = req.json()
        title=str(datos['title'])
        tipo =str(datos['type'])
        mensaje="El titulo es : "+title+" Y el tipo es : "+tipo
       
       #si se pasa del rango y no lo encuentra como puedo programar eso de no encontrar si se pasa
      


    return JsonResponse(mensaje, safe=False)

