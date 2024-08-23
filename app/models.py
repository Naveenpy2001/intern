from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# Profile Model
class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    resume_headline = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.email

# Other Models
class InternSHip(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)

class studentRegister(models.Model):
    first_name = models.CharField(max_length=100)
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
    additional_comments = models.TextField()
    profile_img = models.ImageField(upload_to='uploads/')
    transaction_ID = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

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

class CoursesForms(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    looking_for = models.CharField(max_length=50)
    agree_terms = models.BooleanField()
    course_name = models.CharField(max_length=50, default="", blank=True)

    def __str__(self):
        return self.name
