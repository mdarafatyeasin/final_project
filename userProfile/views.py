from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, UserEditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import userProfileModel
from jobs.models import jobCircularModel,jobApplicationModel
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

# registration
def UserRegistration(request):
    if request.method == "POST":
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            messages.success(request, 'User created successfully!!!')
            reg_form.save(commit=True)
            print(reg_form)
            return redirect('home_page')
    else:
        reg_form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': reg_form})

# login
def UserLogin (request):
    if request.method == "POST":
        login_form = AuthenticationForm(request = request, data = request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, "Welcome Back!")
                login(request, user)
                return redirect('home_page')
            else:
                return redirect('user_registration')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'form':login_form})

# logout
@login_required
def Logout(request):
   logout(request) 
   messages.warning(request, "Please login again")
   return redirect('home_page')

# profile
@login_required
def Profile (request):
    data = request.user
    userProfile = userProfileModel.objects.filter(user=request.user).first()
    user_role = userProfile.role
    if userProfile.role == "employer":
        applications = jobCircularModel.objects.filter(publisher = request.user)
    elif userProfile.role == "job_seeker":
        applications = jobApplicationModel.objects.filter(applicant = request.user)
    else:
        print("User Not Found")
    return render(request, 'profile.html', {'data':data, 'applications':applications, 'user_role': user_role})


# edit profile
@login_required
def editProfile(request):
    if request.method == "POST":
        edit_user = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_user.is_valid():
            edit_user.save()
            # Update userProfileModel if exists, otherwise create new
            profile, created = userProfileModel.objects.get_or_create(user=request.user)
            profile.profile_picture = edit_user.cleaned_data.get('profile_picture')
            profile.save()
            messages.success(request, "Profile Updated")
            return redirect("user_profile")
    else:
        edit_user = UserEditForm(instance=request.user)
    return render(request, 'edit_profile.html', {"form": edit_user})


# change password
@login_required
def changePassword (request):
    if request.method == "POST":
        pass_change_form = PasswordChangeForm(user=request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            update_session_auth_hash(request, pass_change_form.user)
            messages.success(request, "Password Changed")
            return redirect("user_profile")
    else:
        pass_change_form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form":pass_change_form})

@login_required
def viewApplication(request):
    all_applications = jobApplicationModel.objects.all()
    return render(request, "all_applications.html", {"all_applications":all_applications})

def viewApplicant(request, id):
    user = User.objects.get(id = id)
    user_all_application = jobApplicationModel.objects.filter(applicant = user)
    for application in user_all_application:
        if application == user:
            print("got it")
        else:
            print('Oh no!')
    return redirect("applications")

