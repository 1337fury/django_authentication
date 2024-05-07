from django.shortcuts import render
from .forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/sign_up.html", {"form": form})