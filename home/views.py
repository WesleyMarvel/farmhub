from django.shortcuts import render
from signup.views import register
from signup.models import Member, Profile
from django.contrib.auth.models import User


# Create your views here.
def home(request):
	
	if request.method == 'GET':

		deals = Profile.objects.all()

		members = Member.objects.all()

		return render(request, 'home.html', {"deals": deals, "members":members})
	
def viewproposal(request, profile_id, member_id):

	business_proposal = Profile.objects.get(pk=profile_id)

	member = Member.objects.get(pk=member_id)

	return render(request, 'proposal.html', {"business_proposal": business_proposal, "member":member})

