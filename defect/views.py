from django.shortcuts import render
from django.views import generic
from .models import Defect, Category

# Create your views here.

def_per_page = 10

def defect_list(request):
    defects = Defect.objects.all()
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
        'defects': defects
    }
    paginate_by = def_per_page
    return render(
        request, 'defect/defect_list.html', context)

def dashboard(request):
    defects = Defect.objects.all().order_by("-reported_on")[:10]
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
        'defects': defects
    }
    paginate_by = def_per_page
    return render(
        request, 'defect/dash.html', context)

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"

class DashList(generic.ListView):
    queryset = Defect.objects.all().order_by("-reported_on")[:2]
    template_name = "dash.html"

