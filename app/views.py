from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DeleteView,UpdateView,DetailView,CreateView
from django.http import HttpResponse
from app.models import *
from django.urls import reverse_lazy
# Create your views here.

class home(TemplateView):
    template_name='app/home.html'

class Schoolist(ListView):
    model=School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='sclobj'
    success_url=reverse_lazy('Schoolist')