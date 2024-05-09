from django.shortcuts import render
from .forms import RegistrationForm
from .forms import PostForm
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

@login_required(login_url="create_post")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # commit=False means that the Post object is created but not saved to the database
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
    return render(request, "main/create_post.html", {"form": form})