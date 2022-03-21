from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from signup.models import Member
from django.contrib import messages

# Create your views here.
def login(request):
	if request.method == 'GET':

		return render(request, 'login.html')

	if request.method =='POST':

		username = request.POST['username']

		password = request.POST['password']

		user = auth.authenticate(request, username=username, password=password)
		
		if user is not None:  
			
			auth.login(request, user)
			
			return redirect('home')
			
		else:
			
			messages.info(request, 'Can not authenticate this user, Check your password and email')
			
			return redirect('login')

def logout(request):
	
	auth.logout(request)
	
	return redirect('login')