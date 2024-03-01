from django import forms
from . import models

# write forms here
class postCircularForm(forms.ModelForm):
    last_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = models.jobCircularModel
        fields = ["job_title", "description", "requirements", "location", "company_name", "last_date", "vacancy", "salary", "job_category"]


class jobApplicationForm(forms.ModelForm):
    class Meta:
        model = models.jobApplicationModel
        fields = ['cover_letter', 'resume']


class jobCategoryForm(forms.ModelForm):
    class Meta:
        model = models.jobCategoryModel
        fields = "__all__"

class editCircularForm(forms.ModelForm):
    class Meta:
        model = models.jobCircularModel
        fields = ["job_title", "description", "requirements", "location", "company_name", "last_date", "vacancy", "salary", "job_category"]