import cloudinary
from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator, EmptyPage
from django.views import generic
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks
from .models import Defect, Category, Update
from .forms import UpdateForm, DefectForm, CategoryForm


def defect_list(request, page=1):
    """
    Renders a filtered list of defects in :model:`defect` depending on
    the GET request and displays them in a page of 15.

    **Context**

    ``defects``
        The filtered instances of :model:`defect.Defect`.
    ``categories``
        All instances of :model:`defect.Categories`.
    ``users``
        All instances of :model:`auth.User`.
    ``prefill``
        Previously selected filter criteria.

    **Template**

    :template:`defect/defect_list.html`
    """
    users = User.objects.all()
    defects = Defect.objects.all()
    categories = Category.objects.all()
    title_contains = request.GET.get('title_contains')
    body_contains = request.GET.get('body_contains')
    category_is = request.GET.get('category')
    status_is = request.GET.get('status')
    author_is = request.GET.get('author')
    sort_by = request.GET.get('date_sort')
    if title_contains is None:
        title_contains = ''
    if body_contains is None:
        body_contains = ''
    if title_contains != '' and title_contains is not None:
        defects = defects.filter(title__icontains=title_contains)
    if body_contains != '' and body_contains is not None:
        defects = defects.filter(body__icontains=body_contains)
    if category_is != '' and category_is != 'all' and category_is is not None:
        defects = defects.filter(category=category_is)
    if status_is != '' and status_is != 'all' and category_is is not None:
        defects = defects.filter(status=status_is)
    if author_is != '' and author_is != 'all' and author_is is not None:
        defects = defects.filter(author=author_is)
    if sort_by != '' and sort_by is not None:
        if sort_by == 'asc':
            defects = defects.order_by('reported_on')
        if sort_by == 'dsc':
            defects = defects.order_by('-reported_on')

    paginator = Paginator(defects, 15)

    try:
        defects = paginator.page(page)
    except EmptyPage:
        defects = paginator.page(paginator.num_pages)

    if category_is != 'all' and category_is is not None:
        category_is = int(category_is)
    if status_is != 'all' and status_is is not None:
        status_is = int(status_is)
    if author_is != 'all' and author_is is not None:
        author_is = int(author_is)

    prefill = {
        'category_is': category_is,
        'title_contains': title_contains,
        'body_contains': body_contains,
        'author_is': author_is,
        'status_is': status_is,
        'sort_by': sort_by,
    }

    context = {
        'defects': defects,
        'categories': categories,
        'users': users,
        'prefill': prefill,
    }
    return render(
        request, 'defect/defect_list.html', context)


def dashboard(request):
    """
    Renders the last 5 instances of :model:`defect.Defect` and the last 5
    instances of :model:`defect.Update`.

    **Context**
    ``defects``
        The last 5 instances of :model:`defect.Defect`.
    ``updates``
        The last 5 instances of :model:`defect.Update`.
    **Template**
    :template:`defect/dash.html`
    """
    defects = Defect.objects.filter(status=0).order_by("-reported_on")[:5]
    updates = Update.objects.all().order_by("-created_on")[:5]
    context = {
        'defects': defects,
        'updates': updates,
    }
    return render(
        request, 'defect/dash.html', context)


def defect_detail(request, defect_id):
    """
    Renders an individual instance of :model:`defect.Defect` and related instances
    of :model:`defect.Update` with a form for adding a new instance of
    :model:`defect.Update`.

    **Context**

    ``defect``
        An instance of :model:`defect.Defect`.
    ``updates``
        All instances of :model:`defect.Update` related to the defect.
    ``update_count``
        A count of updates for this defect.
    ``update_form``
        An instance of :form:`defect.UpdateForm`.
    ``update_latest``
        The last instance of :model:`defect.Update` related to the defect.

    **Template**

    :template:`defect/defect_detail.html`
    """
    defect = get_object_or_404(Defect.objects.all(), defect_id=defect_id)
    updates = defect.updates.all().order_by("created_on")
    update_count = defect.updates.count()
    update_latest = updates.all().last()
    if request.method == "POST":
        update_form = UpdateForm(request.POST, request.FILES)
        if update_form.is_valid():
            update = update_form.save(commit=False)
            update.author = request.user
            update.defect = defect
            if len(update.body) > 30:
                update.excerpt = update.body[:27] + "..."
            else:
                update.excerpt = update.body
            print(update)
            defect.status = update.resolution
            defect.save()
            update.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Update submitted'
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
            'update_latest': update_latest,
        },)


def update_edit(request, defect_id, update_id):
    """
    Display an individual update for edit.

    **Context**

    ``defect``
        An instance of :model:`defect.Defect`.
    ``updates``
        All instances of :model:`defect.Update` related to the defect.
    ``update_form``
        An instance of :form:`defect.UpdateForm`.
    """
    if request.method == 'POST':
        update = get_object_or_404(Update, pk=update_id)
        defect = update.defect
        update_form = UpdateForm(data=request.POST, instance=update)

        if update_form.is_valid() and update.author == request.user:
            update = update_form.save(commit=False)
            update.defect = defect
            update.save()
            messages.add_message(
                request, messages.SUCCESS, 'Update successfully edited!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error editing update!')

    return HttpResponseRedirect(reverse('def_detail', args=[defect_id]))


def update_delete(request, defect_id, update_id):
    """
    Delete an individual update.

    **Context**

    ``defect``
        An instance of :model:`defect.Defect`.
    ``updates``
        All instances of :model:`defect.Update` related to the defect.

    **Template**

    """
    defect = get_object_or_404(Defect, defect_id=defect_id)
    update = get_object_or_404(Update, pk=update_id)

    if update.author == request.user:
        update.delete()
        messages.add_message(request, messages.SUCCESS, 'Update deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own updates!')

    return HttpResponseRedirect(reverse('def_detail', args=[defect_id]))


def log_defect(request):
    """
    Render a form for adding an instance of :model:`defect.Defect`.

    **Context**

    ``categories``
        All instances of :model:`defect.Category`.
    ``defect_form``
        An instance of :form:`defect.DefectForm`.

    **Template**

    :template:`defect/log_defect.html`
    """
    categories = Category.objects.all()

    if request.method == "POST":
        defect_form = DefectForm(request.POST, request.FILES)
        if defect_form.is_valid():
            defect = defect_form.save(commit=False)
            defect.author = request.user
            if len(defect.body) > 30:
                defect.excerpt = defect.body[:27] + "..."
            else:
                defect.excerpt = defect.body
            if len(defect.title) > 30:
                defect.trunc_title = defect.title[:27] + "..."
            else:
                defect.trunc_title = defect.title
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
    Renders a list of all instances of :model:`defect.Category` with
    a form to add more.

    **Context**

    ``categories``
        All instances of :model:`defect.category`.
    ``category_form``
        An instance of :forms:`defect.CategoryForm`.
    **Template**

    :template:`defect/category_list.html`
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


def custom_404(request, exception):
    """
    Renders a custom 404 page

    **Template**

    :template:`404.html`
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Renders a custom 500 page

    **Template**

    :template:`500.html`
    """
    return render(request, '500.html', status=500)
