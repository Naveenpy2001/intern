"""
URL configuration for internship project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('CorporateLogin',views.CorporateLogin),
    path('',views.internshipPage),
    path('studentDashboard',views.studentDashboard),
    path('studentLogin',views.studentLogin),
    path('registrationForm',views.registrationForm),
    path('angular',views.angular),
    path('aws',views.aws),
    path('azure',views.azure),
    path('bigdata',views.bigdata),
    path('cloud',views.cloud),
    path('dataScience',views.dataScience),
    path('dotnet',views.dotnet),
    path('Java',views.Java),
    path('php',views.php),
    path('pythonPage',views.pythonPage),
    path('reactJs',views.reactJs),
    path('salesforce',views.salesforce),
    path('sap',views.sap),
    path('profileDashboard',views.profileDashboard),

    path('success/', views.success_view, name='success'),

    # main URLS
    path('enquiry_view',views.enquiry_view),
    path('register/', views.register, name='register'),
    path('login/', views.student_login, name='student_login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),



    path('course-form/', views.course_form_view, name='course_form'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    