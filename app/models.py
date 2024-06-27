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