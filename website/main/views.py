from django.shortcuts import render
from .forms import RegistrationForm
# import login_required decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

@login_required(login_url="login")
def index(request):
    return render(request, "main/index.html")

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
    else:
        form = RegistrationForm()
    return render(request, "registration/sign_up.html", {"form": form})