from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import UsersCreationForm
from account.models import User


def register(request):
    context = {
        'form': UsersCreationForm()
    }
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('account:login')
        context['form'] = form
    return render(request, 'login.html', context)


def login_page(request):
    if request.method == 'POST':
        model = User.objects.all()
        form = AuthenticationForm(data=request.POST)
        if model.all().filter(email__exact=form.data['username']):
            users = model.first()
            user = authenticate(username=users, password=form.data['password'])
            if user is not None:
                login(request, user)
                return redirect('polls:home')
        else:
            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user is not None:
                login(request, user)
                return redirect('polls:home')

    return render(request, 'login.html')


