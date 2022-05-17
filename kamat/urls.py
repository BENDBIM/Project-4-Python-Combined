from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
	path("kamat/", include("kamat.urls")),
    path("blog/", include("blog.urls")),
]



