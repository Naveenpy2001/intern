from django.db import models

# Create your models here.
class InternSHip(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    

class studentRegister(models.Model):
    firstr_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    street_address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    student_email = models.EmailField()
    alt_phoneNo = models.CharField(max_length=100)
    selected_course = models.CharField(max_length=100)
    referred_HR = models.CharField(max_length=100)
    addition_comments = models.TextField()
    profile_img = models.ImageField(upload_to='uploads/')
    transaction_ID = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)



# models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    resume_headline = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name



from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    looking_for = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


from django.db import models

class CoursesForms(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    looking_for = models.CharField(max_length=50)
    agree_terms = models.BooleanField()
    course_name = models.CharField(max_length=50, default="",blank=True)

    def __str__(self):
        return self.name
