from django.urls import path
from .views import post_circular,CircularDetails,JobApplication,add_category,deleteCircular,editCircular,DeleteJobApplication

urlpatterns = [
    path("post_circular", post_circular, name="post_circular"),
    path("circular_details/<int:id>", CircularDetails.as_view(), name="circular_details"),
    path("circular_details/job_application/<int:id>", JobApplication, name="job_application"),
    path("add_category", add_category, name="add_category"),
    path("delete_circular/delete/<int:id>", deleteCircular, name="delete_circular"),
    path("edit_circular/edit/<int:id>", editCircular, name="edit_circular"),
    path("delete_application/delete/<int:id>", DeleteJobApplication, name="delete_application"),
]