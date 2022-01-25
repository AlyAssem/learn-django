from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticates if the user is registered.
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            context["authentication_error"] = 'Invalid username or password'

    return render(request, "accounts/login.html", context)


def logout_view(request):
    print('hello logout view')
    context = {}
    if request.method == "POST":
        logout(request)
        return redirect('/login/')

    return render(request, "accounts/logout.html", context)
