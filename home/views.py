from django.shortcuts import render
from signup.views import register
from signup.models import Member, Profile
from django.contrib.auth.models import User


# Create your views here.
def home(request):
	
	if request.method == 'GET':

		deals = Profile.objects.all()

		return render(request, 'home.html', {"deals": deals})
	
def viewproposal(request, profile_id):

	business_proposal = Profile.objects.get(pk=profile_id)

	return render(request, 'proposal.html', {"business_proposal": business_proposal})

