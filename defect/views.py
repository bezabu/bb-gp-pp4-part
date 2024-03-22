from django.shortcuts import render
from django.views import generic
from .models import Defect, Category

# Create your views here.

class DefectList(generic.ListView):
    queryset = Defect.objects.all().order_by("-reported_on")
    template_name = "defect_list.html"

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"

class DashList(generic.ListView):
    queryset = Defect.objects.all().order_by("-reported_on")[:2]
    template_name = "dash.html"