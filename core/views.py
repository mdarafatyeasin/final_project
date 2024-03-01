from django.shortcuts import render
from jobs.models import jobCircularModel,jobCategoryModel
# Create your views here.

def HomePage(request):
    return render(request, 'index.html')

def ViewJobs(request, category_slug=None):
    all_circular = jobCircularModel.objects.all()
    all_jobs_category = jobCategoryModel.objects.all()

    if category_slug is not None:
        category = jobCategoryModel.objects.get(slug=category_slug)
        all_circular = category.jobcircularmodel_set.all()  # Filter using the related name

    return render(request, 'all_jobs.html', {"all_circular": all_circular, "all_jobs_category": all_jobs_category})

