from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm

from .models import Item, UserExtend, Images

from django.contrib.auth import authenticate, login

# Create your views here.

class LoginPage(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        return render(request, 'base/login.html',{
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, 'base/login.html', {
            'form': form
        })


class Register(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm()
        return render(request, 'base/register.html', {
            'form': form
        })

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            register = User(username=username, password=make_password(password), first_name=first_name, last_name=last_name)
            register.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                new_user = UserExtend(user=user)
                new_user.save()
                login(request, user)
                return redirect('home')

        return render(request, 'base/register.html', {
            'form': form
        })



class HomePage(View):
    def get(self, request):
        item_query = Item.objects.filter(status=True).order_by('-created')
        if len(item_query) >= 5:
            newest_item = []
            for i in range(5):
                newest_item.append(item_query[i])
        else:
            newest_item = item_query
        return render(request, 'base/home.html', {
            'new_item': newest_item,
        })
    
    def post(self, request):
        pass


class ItemDetail(View):
    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        item_image = Images.objects.filter(item=item)
        return render(request, 'base/detail.html', {
            'item': item,
            'images': item_image
        })