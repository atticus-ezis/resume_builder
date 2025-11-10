"""
URL configuration for resume_helper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from builder import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.build_resume, name="build_resume"),
    path("download/resume/", views.resume_pdf_download, name="resume_pdf_download"),
    path(
        "download/cover-letter/",
        views.cover_letter_pdf_download,
        name="cover_letter_pdf_download",
    ),
    path("app-search/", views.view_job_applications, name="view_job_applications"),
    path(
        "app-detail/<int:id>/",
        views.job_application_detail,
        name="job_application_detail",
    ),
]
