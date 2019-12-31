from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from workshop.models import Comment
from workshop.forms import CommentForm, UserForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user_form = CommentForm(request.POST)

    if request.method == "POST":
        user_form = CommentForm(request.POST)

        if user_form.is_valid():
            user_form.save()

    return render(request, 'home.html', {"form": user_form})

def log(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)

            login(request, authenticate(
                 username = user_form.cleaned_data["username"],
                 password = user_form.cleaned_data["password"]
            ))

    return render(request, 'log.html',{
        "user_form": user_form,
    })

def account(request):
    return redirect(account_home)

def account_home(request):
    return render(request, 'account/home.html', {})
