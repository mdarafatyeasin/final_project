from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class jobCategoryModel(models.Model):
    category = models.CharField(max_length = 100, null=True, blank=True)
    slug = models.SlugField(max_length = 100, null=True, blank=True, unique = True)
    
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Job Category"

class jobCircularModel(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now_add=False)
    vacancy = models.IntegerField()
    salary = models.IntegerField()
    job_category = models.ManyToManyField(jobCategoryModel)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name_plural = "Job Circular"


class jobApplicationModel(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job_circular = models.ForeignKey(jobCircularModel, on_delete=models.CASCADE, )
    # extra part
    cover_letter = models.TextField(default=None)
    resume = models.FileField(upload_to="jobs/resume/", default=None)

    def __str__(self):
        return self.job_circular.publisher.username

    class Meta:
        verbose_name_plural = "Job Applications"
