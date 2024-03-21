from django.shortcuts import render
from django.views import generic
from .models import Defect, Category

# Create your views here.

class DefectList(generic.ListView):
    queryset = Defect.objects.all()
    template_name = "defect_list.html"