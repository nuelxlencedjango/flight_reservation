from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import *

def loginAction(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "flights/login.html", 
            {"message": "Invalid username and/or password." })    
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, "flights/login.html")   



def registration(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensuring password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "flights/register.html", {
                "message": "Passwords must match." })

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()

        except:
            return render(request, "flights/register.html", {
                "message": "Username already taken." }) 

        login(request, user) 
        return HttpResponseRedirect(reverse("index"))  


    else:
        return render(request, "flights/register.html")         



def logoutAction(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
