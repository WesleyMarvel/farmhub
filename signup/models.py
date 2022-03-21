from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        
        return f"{self.user}"

class Profile(models.Model):
	
	member = models.ForeignKey(Member, on_delete=models.CASCADE, null=False, related_name="member")

	property_name = models.CharField(max_length = 50, null = False)

	property_description = models.TextField(null = False)

	partnership_proposal = models.TextField(max_length = 155, null = False)

	property_image = models.ImageField(null = False)

	status_is_approved = models.BooleanField(default = False)

	def __str__(self):

		return f"{self.member}"
