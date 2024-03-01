from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.views.generic import DetailView
from . import models
from django.db import IntegrityError
from userProfile.models import userProfileModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.

# email
def send_confirmation_email(user, circular, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'circular' : circular,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()


# Add Category
def add_category(request):
    if request.method == "POST":
        add_category_form = forms.jobCategoryForm(request.POST)
        if add_category_form.is_valid():
            messages.success(request, "category added successfully")
            add_category_form.save()
            return redirect("add_category")
    else:
        add_category_form = forms.jobCategoryForm()
    return render (request, 'add_category.html', {"form":add_category_form})

# Post Circular
def post_circular(request):
    userProfile = userProfileModel.objects.filter(user=request.user).first()

    if userProfile:    
        if userProfile.role == "employer":
            if request.method == "POST":
                add_circular_form = forms.postCircularForm(request.POST)
                if add_circular_form.is_valid():
                    add_circular_form.instance.publisher = request.user
                    messages.success(request, "Circular posted successfully")
                    add_circular_form.save()
                    return redirect("home_page")
            else:
                add_circular_form = forms.postCircularForm()
            return render(request, "add_circular.html", {"form": add_circular_form})
        else:
            messages.warning(request, "You don't have access. Only employers can access here")
            return redirect("home_page")
    else:
        messages.warning(request, "User profile not found")
        return redirect("home_page")

# Circular Details
class CircularDetails(DetailView):
    model = models.jobCircularModel
    pk_url_kwarg = 'id'
    template_name = 'circular_details.html'

# DELETE Circular
def deleteCircular(request, id):
    circular = models.jobCircularModel.objects.get(pk = id)
    circular.delete()
    return redirect("user_profile")

# Job Applications
# def JobApplication(request, id):
#     user = request.user
#     circular = models.jobCircularModel.objects.get(id=id)
#     if user:
#         try:
#             application = models.jobApplicationModel.objects.create(applicant=user, job_circular=circular)
#             messages.success(request, "Applied Successfully 🌟🌟")
#             print(circular)
#             send_transaction_email(request.user, circular, "Job Application", "application_confirmation_email.html")
#         except IntegrityError:
#             messages.warning(request, "You have already applied for this job.")
    
#     return redirect('home_page')

def JobApplication(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        form = forms.jobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            circular = get_object_or_404(models.jobCircularModel, id=id)
            try:
                application = form.save(commit=False)
                application.applicant = user
                application.job_circular = circular
                application.save()
                messages.success(request, "Applied Successfully 🌟🌟")
                send_confirmation_email(user, circular, "Job Application", "application_confirmation_email.html")
                return redirect('all_jobs')
            except IntegrityError:
                messages.warning(request, "You have already applied for this job.")
        else:
            messages.warning(request, "Invalid form submission. Please check your inputs.")
    else:
        form = forms.jobApplicationForm()

    return render(request, 'job_application_form.html', {'form': form})


# DELETE job application
def DeleteJobApplication(request, id):
    application = models.jobApplicationModel.objects.get(pk=id)
    if application:
        messages.success(request, "Application delete successfully")
        application.delete()
    return redirect("user_profile")

# EDIT job application (create job application model then do all functionality before that also update the JobApplication)

# edit circular
@login_required
def editCircular(request, id):
    circular_instance = get_object_or_404(models.jobCircularModel, id=id)
    if request.method == "POST":
        edit_circular = forms.editCircularForm(request.POST, instance=circular_instance)
        if edit_circular.is_valid():
            messages.success(request, "Circular updated")
            edit_circular.save()
            return redirect("user_profile")
    else:
        edit_circular = forms.editCircularForm(instance=circular_instance)
    return render(request, 'add_circular.html', {"form":edit_circular})

