from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from workshop.models import Comment, Speciality
from workshop.forms import CommentForm, UserForm, SubmitForm
from django.contrib.auth.models import User
from .models import Submit

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
            return redirect(contact)

    return render(request, 'log.html',{
        "user_form": user_form,
    })

@login_required(login_url='/login/')
def account_home(request):
    try:
        accepted = Submit.objects.get(sub = request.user).accepted
        print(accepted)
    except :
        accepted = None


    return render(request, 'account/home.html', {"accepted":accepted})

def data(request):
    specialities = ["AI","ML","DM","DL"]
    for speciality in specialities :
        b = Speciality.objects.create(name= speciality, parent_id = 1)

    return render(request, 'data.html')

@login_required(login_url='/login/')
def submit(request):
    form= SubmitForm()
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.sub = request.user
            doc.save()
            return HttpResponseRedirect('/login/account/')

    return render(request, 'account/submit.html', {'form':form})

def contact(request):
    return render(request, 'contact.html', {})

def program(request):
    return render(request, 'program.html', {})
