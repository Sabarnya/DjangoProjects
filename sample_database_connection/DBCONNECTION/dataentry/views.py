from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):

    if request.method== 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']

        user=User.objects.create_user(firstname=firstname, lastname=lastname, email=email)
        user.save()
        print('user created')
        return redirect('/')
    else: 
        return render(request,'register.html')