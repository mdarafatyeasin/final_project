from django.db import models
from django.contrib.auth.models import User

# constructor 
USER_ROLE = [
    ('employer', 'Post Jobs'),
    ('job_seeker', 'Apply for Jobs'),
]
# Create your models here.
class userProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="userProfile/profile_picture/")
    role = models.CharField(choices = USER_ROLE, max_length = 20)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name_plural = "User Profile"