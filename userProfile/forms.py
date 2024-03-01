from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from .models import userProfileModel

USER_ROLE = [
    ('employer', 'Post Jobs'),
    ('job_seeker', 'Apply for Jobs'),
]

class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=USER_ROLE)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        role = self.cleaned_data['role']
        user_profile = userProfileModel.objects.create(user=user, role=role)
        return user

class UserEditForm(forms.ModelForm):
    profile_picture = forms.ImageField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','profile_picture']