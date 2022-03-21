from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Member, Profile
from django.http import HttpResponse, Http404

# Create your views here.
def register(request):
	
		if request.method == "GET":
			return render(request, 'signup.html')
			
		if request.method == "POST" and request.FILES:
			
			first_name = request.POST["first_name"]
			
			last_name = request.POST["last_name"]
			
			username = request.POST["username"]
			
			email = request.POST["email"]

			property_name = request.POST["property_name"]

			property_description = request.POST["property_description"]

			property_image = request.FILES["property_image"]

			partnership_proposal = request.POST["partnership_proposal"]
			
			password = request.POST["password"]
			
			cpassword = request.POST["cpassword"]
			
			if (password == cpassword):
				
				if User.objects.filter(username=username).exists():
					
					messages.info(request, username + ' this username is taken, please try another one')
					
					return redirect('register')
					
				elif User.objects.filter(email=email).exists():
					
					messages.info(request, email + ' this email is taken, please try another one')
					
					return redirect('register')
					
				else:
						
					user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
						
					user.set_password(password)
						
					user.save()

					messages.info(request, 'Registration Successful!!')

					member = Member(user=user)

					member.save()

					profile = Profile(member=member, property_name=property_name, property_description=property_description, partnership_proposal=partnership_proposal, property_image=property_image)

					profile.save()

					return redirect('login')
					
			else:
				
				messages.info(request, 'Passwords do not match')
				
				return redirect('register')
				

