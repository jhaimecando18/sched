from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import facultyForm


# Ref 1: https://stackoverflow.com/questions/2245895/is-there-a-simple-way-to-get-group-names-of-a-user-in-django
@login_required(login_url='/account/login/')
def home(request):

    return render(request, 'home/home.html', {})

@login_required
def prof(request):
    return render(request, 'home/faculty-form.html', {})

