from django.shortcuts import render

from .models import studentRegister

# email send conf settings and modules
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'internship-page.html')

def CorporateLogin(request):
    return render(request,'Corporate-login.html')


def internshipPage(request):
    language = [
        "select",
        "Python",
        "Java",
        "Big data",
        'React JS',
        "Angular",
        "AWS",
        "Data Science",
        "Sales Force",
        "Azure",
        "Cloud",
        " .Net",
        "Digital Marketing",
        "Web Development",
        "Machine Learning",
        "Other."
 ]
    
    return render(request,'internship-page.html',{'language':language})

def studentDashboard(request):
    return render(request,'student-dashboard.html')

def studentLogin(request):
    return render(request,'student-login.html')

def profileDashboard(request):
    return render(request,'profile-dashboard.html')

def registrationForm(request):
    languages = [
        "select",
        "Python",
        "Java",
        "Big data",
        'React JS',
        "Angular",
        "AWS",
        "Data Science",
        "Sales Force",
        "Azure",
        "Cloud",
        " .Net",
        "Digital Marketing",
        "Web Development",
        "Machine Learning",
        "Other."
 ]
    if request.method == 'POST':
        firstr_name = request.POST['firstname']
        last_name = request.POST['last-name']
        date = request.POST['date']
        gender = request.POST['gender']
        street_address = request.POST['address']
        street_address2 = request.POST['address_2']
        city = request.POST['city']
        postal_code = request.POST['postal']
        state = request.POST['state']
        student_email = request.POST['stdemail']
        alt_phoneNo = request.POST['phone']
        selected_course = request.POST['course']
        referred_HR = request.POST['hr_name']
        addition_comments = request.POST['msg']
        profile_img = request.FILES.get('profile_img')
        transaction_ID = request.POST['trans_id']
        std_form = studentRegister.objects.create(firstr_name=firstr_name,last_name=last_name,date=date,gender=gender,street_address=street_address,street_address2=street_address2,city=city,postal_code=postal_code,state=state,student_email=student_email,alt_phoneNo=alt_phoneNo,selected_course=selected_course,referred_HR=referred_HR,addition_comments=addition_comments,profile_img=profile_img,transaction_ID=transaction_ID,).save()

        user_email_subject = 'Thank you for registering!'
        user_email_message = 'Dear {},\n\nThank you for registering with us. We will get back to you soon.'.format(firstr_name)
        send_mail(user_email_subject, user_email_message, settings.EMAIL_HOST_USER, [student_email], fail_silently=False)
    
        # Send email to admin
        admin_email_subject = 'New registration: {}'.format(firstr_name)
        admin_email_message = 'A new user has registered:\nName: {}\nPhone: {}\nEmail: {}\nCourse Name: {}'.format(firstr_name, alt_phoneNo, student_email,selected_course)
        send_mail(admin_email_subject, admin_email_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)

        return render(request, 'success.html')

    return render(request,'registration-form.html',{"languages":languages})

def angular(request):
    return render(request,'angular.html')


def aws(request):
    return render(request,'aws.html')

def azure(request):
    return render(request,'azure.html')

def bigdata(request):
    return render(request,'bigdata.html')

def cloud(request):
    return render(request,'cloud.html')

def dotnet(request):
    return render(request,'dot-net.html')

def dataScience(request):
    return render(request,'data-science.html')

def Java(request):
    return render(request,'Java.html')

def php(request):
    return render(request,'php.html')

def pythonPage(request):
    return render(request,'python-page.html')

def reactJs(request):
    return render(request,'reactJs.html')

def salesforce(request):
    return render(request,'salesforce.html')

def sap(request):
    return render(request,'sap.html')


def success_view(request):
    return render(request, 'success.html')

from django.shortcuts import render, redirect
from .models import Enquiry

def enquiry_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        course = request.POST.get('course')
        country = request.POST.get('country')
        state = request.POST.get('state')
        looking_for = request.POST.get('looking_for')

        Enquiry.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            course=course,
            country=country,
            state=state,
            looking_for=looking_for
        )
        return redirect('success')  # Redirect to a success page or another view
    return render(request, 'internship-page.html')



# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Set username to email for unique constraint
            user.save()
            Profile.objects.create(
                user=user,
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                phone_number=form.cleaned_data.get('phone_number'),
                resume=form.cleaned_data.get('resume'),
                resume_headline=form.cleaned_data.get('resume_headline'),
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'student-login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'student-login.html', {'form': form})

@login_required
def student_dashboard(request):
    return render(request, 'student-dashboard.html')




from django.shortcuts import render, redirect
from .forms import CoursesFormsForm

def course_form_view(request):
    if request.method == 'POST':
        form = CoursesFormsForm(request.POST)
        if form.is_valid():
            # course_form = form.save(commit=False)
            course_form = form.save()
            course_form.course_name = "Angular"  # Set the course name here
            course_form.save()
            return redirect('success')  # Redirect to a success page
        else:
            print(form.errors)
    else:
        form = CoursesFormsForm()

    return render(request, 'angular.html', {'form': form})

def course_form_view(request):
    if request.method == 'POST':
        form = CoursesFormsForm(request.POST)
        if form.is_valid():
            # course_form = form.save(commit=False)
            course_form = form.save()
            course_form.course_name = "AWS"  # Set the course name here
            course_form.save()
            return redirect('success')  # Redirect to a success page
        else:
            print(form.errors)
    else:
        form = CoursesFormsForm()

    return render(request, 'aws.html', {'form': form})
