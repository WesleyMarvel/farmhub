from django.shortcuts import render
from signup.models import Member
from django.contrib.auth.models import User, auth
from .models import Partners 
import random
from django.contrib import messages
# Create your views here.
def connect(request, member_id):

    partner1 = request.user.member

    partner2 = Member.objects.get(pk=member_id)

    code = "FARMH" + str(random.randint(1,9999))

    connect = Partners(partner1=partner1, partner2=partner2, partnership_code=code)

    connect.save()

    messages.info(request, 'Connection request submitted to admin')

    return render(request, 'connect.html', {"code":code})