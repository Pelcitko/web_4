from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from Shop.forms import UserForm
from Shop.models import Rose, Profile


def index(request):
    return render(request, 'Shop/index.html')

class RoseList(ListView):
    model = Rose

def rose_list(request):
    queryset_list = Rose.objects.all()
    paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list': queryset,
        'title': "Nabídka růží",
        'page_request_var': page_request_var,
    }

    return render(request, 'Shop/rose-list.html', context)

class RoseDetail(DetailView):
    model = Rose

@login_required(login_url='/login/')
def profile(request, saved):
    prof = Profile(user=request.user)
    return render(request, 'Shop/profile.html', {'profile': prof})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'accounts/profile/', {'user': user})
    context = {"form": form,}
    return render(request, 'registration/register.html', context)