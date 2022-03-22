from django.db import models
from signup.models import Member

# Create your models here.
class Partners(models.Model):

    partner1 = models.ForeignKey(Member, on_delete=models.CASCADE, null=False, related_name="member0")

    partner2 = models.ForeignKey(Member, on_delete=models.CASCADE, null=False, related_name="member1")

    partnership_code = models.TextField(null=False)

    partnership_report = models.TextField(null = True)

    approve_connection = models.BooleanField(default = False)

    def __str__(self):
        
        return f"{self.partnership_code}"