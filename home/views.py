from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError


@login_required(login_url='/login/')
def index(request):
    user = request.user

    if user.user_role == 'Q':
        return HttpResponseRedirect(reverse("suiviqualite:index"))

    elif user.user_role == 'P':
        return HttpResponseRedirect(reverse("suiviproduction:index"))
  
    else :
        return render(request, 'home/home.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        user_role = request.POST["user_role"]
        password = request.POST["password"]
        user = authenticate(request, username=user_role, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home:index"))
        else:
            return render(request, "home/login.html", {
                "message": "Identifiants incorrects"
            })
    else:
        return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return render(request, "home/login.html")