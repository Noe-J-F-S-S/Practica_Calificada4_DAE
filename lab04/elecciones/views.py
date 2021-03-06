from ast import arg
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse

# from django.shortcuts import render

from .models import Candidato, Region

# Create your views here.

def index(request):
    latest_question_list = Region.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'elecciones/index.html', context)

def detalle(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'elecciones/detalle.html',{'region': region})

def detCandidato(request, candidato_id):
    candidato = get_object_or_404(Candidato, pk=candidato_id)
    return render(request, 'elecciones/detCandidato.html',{'candidato': candidato})
