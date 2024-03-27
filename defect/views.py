from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator, EmptyPage
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.http import HttpResponseRedirect
import cloudinary
from cloudinary.forms import cl_init_js_callbacks  
from .models import Defect, Category, Update
from .forms import UpdateForm, DefectForm, CategoryForm

# Create your views here.

def_per_page = 10

def defect_list(request, page=1):
    defects = Defect.objects.all()
    categories = Category.objects.all()
    #page = request.GET.get('page', 1)
    paginator = Paginator(defects, 15)

    try:
        defects = paginator.page(page)
    except EmptyPage:
        defects = paginator.page(paginator.num_pages)

    context = {
        'defects': defects,
        'categories': categories,
    }
    return render(
        request, 'defect/defect_list.html', context)

def dashboard(request):
    defects = Defect.objects.filter(status=0).order_by("-reported_on")[:5]
    updates = Update.objects.all().order_by("-created_on")[:5]
    context = {
        'defects': defects,
        'updates': updates,
    }
    return render(
        request, 'defect/dash.html', context)

def defect_detail(request, defect_id):
    defect = get_object_or_404(Defect.objects.all(), defect_id=defect_id)
    updates = defect.updates.all().order_by("created_on")
    update_count = defect.updates.count()
    if request.method == "POST":
        #update_form = UpdateForm(data=request.POST)
        update_form = UpdateForm(request.POST, request.FILES)
        if update_form.is_valid():
            update = update_form.save(commit=False)
            update.author = request.user
            update.defect = defect
            if len(update.body)>30:
                update.excerpt = update.body[:27] + "..."
            else:
                update.excerpt = update.body
            #update.image_url = cloudinary.uploader.upload(file)
            print(update)
            defect.status = update.resolution
            defect.save()
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
        },)

def update_edit(request, defect_id, update_id):
    """
    view to edit updates
    """
    if request.method == 'POST':
        defect = get_object_or_404(Defect, defect_id=defect_id)
        update = get_object_or_404(Update, update_id=update_id)
        update_form = UpdateForm(data=request.POST, instance=update)

        if update_form.is_valid() and update.author == request.user:
            update = update_form.save(commit=False)
            update.defect = defect
            update.save()
            messages.add_message(request, messages.SUCCESS, 'Update successfully edited!')
        else:
            messages.add_message(request, messages.ERROR, 'Error editing update!')
    
    return HttpResponseRedirect(revese('def_detail', args=[defect_id]))

def update_delete(request, defect_id, update_id):
    """

    """
    defect = get_object_or_404(Defect, defect_id=defect_id)
    update = get_object_or_404(Update, update_id=update_id)

    if update.author == request.user:
        update.delete()
        messages.add_message(request, messages.SUCCESS, 'Update deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own updates!')
    
    return HttpResponseRedirect(reverse('def_detail', args=[defect_id]))

def log_defect(request):
    """
    """
    categories = Category.objects.all()

    if request.method == "POST":
        #defect_form = DefectForm(data=request.POST)
        defect_form = DefectForm(request.POST, request.FILES)
        #file = request.FILES
        if defect_form.is_valid():
            defect = defect_form.save(commit=False)
            defect.author = request.user
            if len(defect.body)>30:
                defect.excerpt = defect.body[:27] + "..."
            else:
                defect.excerpt = defect.body
            
            if len(defect.title)>30:
                defect.trunc_title = defect.title[:27] + "..."
            else:
                defect.trunc_title = defect.title
            #defect.image_url=cloudinary.uploader.upload(request.FILES)
            defect.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Defect logged'
            )


    defect_form = DefectForm()

    return render(
        request,
        'defect/log_defect.html',
        {
            'categories': categories,
            'defect_form': defect_form,
        },
    )

def category_list(request):
    """
    #
    """
    categories = Category.objects.all()

    if request.method == "POST":
        category_form = CategoryForm(data=request.POST)
        if category_form.is_valid():
            category = category_form.save(commit=False)
            
            category.save()
            messages.add_message(
                request, messages.SUCCESS,
                'New category successfully added'
            )
        
    category_form = CategoryForm()

    return render(
        request, 
        'defect/category_list.html', 
        {
            'categories': categories,
            'category_form': category_form,
        },
    )

def user_approval(request):
    """
    """
    users = User.objects.all()
    
    return render(
        request,
        'defect/user_approval.html',
        {
            'users': users,
        }
    )

def home_page(request):
    return render(request, 'defect/index.html')

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category_list.html"

class DashList(generic.ListView):
    queryset = Defect.objects.all().order_by("-reported_on")[:2]
    template_name = "dash.html"

