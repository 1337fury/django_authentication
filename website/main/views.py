from django.shortcuts import render
from .forms import RegistrationForm
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

@login_required(login_url="/login")
def index(request):
    posts = Post.objects.all()
    return render(request, "main/index.html", {"posts": posts})

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, 'Please review the form and correct the errors.')
    else:
        form = RegistrationForm()
    return render(request, "registration/sign_up.html", {"form": form})

@login_required(login_url="/login")
@permission_required("main.add_post", raise_exception=True) # This decorator checks if the user has the add_post permission and raises a PermissionDenied exception if they don't
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

@login_required(login_url="/login")
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
    return redirect("/home")