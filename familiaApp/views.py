from django.shortcuts import render
from django.template import loader
from .models import Familiar
from django.http import HttpResponse

# Create your views here.


def listado_familia(request):
   
    template = loader.get_template('listado_familia.html')
    familiares=Familiar.objects.all()
    print(familiares)
    context = {
        'familiares': familiares,
    }
    return HttpResponse(template.render(context, request))