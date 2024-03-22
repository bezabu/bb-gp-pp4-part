from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Defect, Category, Update

# Create your views here.

def_per_page = 10

def defect_list(request):
    defects = Defect.objects.all()
    categorys = Category.objects.all()
    #update_count = defects.updates.count()
    context = {
        'categorys': categorys,
        'defects': defects,

    }
    paginate_by = def_per_page
    return render(
        request, 'defect/defect_list.html', context)

def dashboard(request):
    defects = Defect.objects.all().order_by("-reported_on")[:10]
    categorys = Category.objects.all()

    context = {
        'categorys': categorys,
        'defects': defects,
    }
    paginate_by = def_per_page
    return render(
        request, 'defect/dash.html', context)

def defect_detail(request, defect_id):
    queryset = Defect.objects.all()
    defects = get_object_or_404(queryset, defect_id=defect_id)
    categorys = Category.objects.all()
    updates = Update.objects.all()
    #update_count = defect.updates.count()
    context = {
        'categorys': categorys,
        'defects': defects,
        'updates': updates,
    }
    paginate_by = def_per_page

    return render(
        request,
        'defect/defect_detail.html',
        {  
            'categorys': categorys,
            'defects': defects,
            'updates': updates,
            #"update_count": update_count,
        },
    )

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"

class DashList(generic.ListView):
    queryset = Defect.objects.all().order_by("-reported_on")[:2]
    template_name = "dash.html"

