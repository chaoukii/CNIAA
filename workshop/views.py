from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from workshop.models import Comment, Speciality
from workshop.forms import CommentForm, UserForm, SubmitForm
from django.contrib.auth.models import User
from .models import Submit
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    user_form = CommentForm(request.POST)
    print(user_form)
    if request.method == "POST":
        user_form = CommentForm(request.POST)
        print(user_form)

        if user_form.is_valid():
            user_form.save()
    print(user_form)
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
            return redirect("account_home")

    return render(request, 'log.html',{
        "user_form": user_form,
    })

@login_required(login_url='/login/')
def account_home(request):
    subject = 'You have been accepted '
    message = 'thank you for waiting your time with us !'
    email_from = settings.EMAIL_HOST_USER
    try:
        accepted = Submit.objects.get(sub = request.user).accepted
        notexist = False
    except :
        notexist = True
        accepted = False

    subs = Submit.objects.all()
    for sub in subs :
        acc = sub.accepted
        if acc == True :
            try:
                email = sub.user.email
                send_mail( subject, message, email_from, [email,] )
                sub.accepted = False
                sub.save()
            except:
                print('No internet !')



    return render(request, 'account/home.html', {
    "accepted":accepted,
    "notexist":notexist,
    })

def people(request):
    return render(request, 'people.html')

@login_required(login_url='/login/')
def submit(request):
    form= SubmitForm()
    subject = 'Thank you for registering to our our event'
    message = 'thank you for registering, you will get a confermation email when if you get accepted, contact us for more informations !'
    email_from = settings.EMAIL_HOST_USER
    email = request.user.email
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            try:
                send_mail( subject, message, email_from, [email,] )
            except:
                print('No internet !')
            doc.sub = request.user
            doc.save()

            return HttpResponseRedirect('/login/account/')



    return render(request, 'account/submit.html', {'form':form})
