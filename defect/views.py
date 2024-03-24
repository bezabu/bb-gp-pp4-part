from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Defect, Category, Update
from .forms import UpdateForm

# Create your views here.

def_per_page = 10

def defect_list(request):
    defects = Defect.objects.all()
    categories = Category.objects.all()
    context = {
        'defects': defects,
        'categories': categories,
    }
    paginate_by = def_per_page
    return render(
        request, 'defect/defect_list.html', context)

def dashboard(request):
    defects = Defect.objects.all().order_by("-reported_on")[:10]
    context = {
        'defects': defects,
    }
    paginate_by = def_per_page
    return render(
        request, 'defect/dash.html', context)

def defect_detail(request, defect_id):
    defect = get_object_or_404(Defect.objects.all(), defect_id=defect_id)
    updates = defect.updates.all().order_by("-created_on")
    update_count = defect.updates.count()
    
    if request.method == "POST":
        update_form = UpdateForm(data=request.POST)
        if update_form.is_valid():
            update = update_form.save(commit=False)
            update.author = request.user
            update.defect = defect
            
            update.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Update added'
            )


    update_form = UpdateForm()

    return render(
        request,
        'defect/defect_detail.html',
        {  
            'defect': defect,
            'updates': updates,
            'update_count': update_count,
            'update_form': update_form,
        },
    )

def home_page(request):
    return render(request, 'defect/index.html')

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"

class DashList(generic.ListView):
    queryset = Defect.objects.all().order_by("-reported_on")[:2]
    template_name = "dash.html"

