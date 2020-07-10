from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import get_in_touch, appoinment, news

# Create your views here.
def HOME(request):
    if request.method == 'POST':
        name = request.POST['your_name']
        phone =request.POST['your_phone']
        email = request.POST['your_email']
        Address =request.POST['your_address']
        time = request.POST['your_time']
        date = request.POST['your_date']
        massage = request.POST['your_message']
        appoin = appoinment(ur_name= name,ur_phone =phone, ur_email =email,
        ur_Address = Address,ur_time = time, ur_date = date, ur_mass = massage  )
        appoin.save()

    return render(request, 'index.html')

def contuct(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email =request.POST['message_email']
        phone =request.POST['Phone']
        subject =request.POST['subjects']
        massage =request.POST['message']
        conact = get_in_touch(massage_name=name, massage_Email= email,
        massage = massage, user_phone =phone, user_subjects= subject)
        conact.save()
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')



def log(request):

    return render(request, 'log.html')

def reg(request):
    if request.method == 'POST':
        # get value 
        first_name = request.POST['f_name']
        last_name = request.POST[' l_name']
        Username = request.POST['username ']
        email = request.POST[' email']
        password = request.POST[' password']
        password2 = request.POST[' password2']

        if password == password2:
            print("password mathch")
            if User.objects.filter(username=username).exists():
                print("user name is not valid ")
                return redirect('Registration')
            else:
                if User.objects.filter(email=email).exists():
                    print("Email is not valid ")
                    return redirect('Registration')
                else:
                    user = User.objects.create_user(first_name = first_name , last_name = last_name , email= email , password=password)
                    user.save()
                    return redirect('LOG_In')
        else:
            print("password not match ")
            return redirect('Registration')
    else:
        return render(request, 'reg.html', {})
        
    return render(request, 'reg.html')


def about(request):
    return render(request, 'about.html')



def blog(request):
    return render(request, 'blog.html')


def service(request):
    return render(request, 'service.html')


def price(request):
    return render(request, 'pricing.html')


def bdetails(request):
    return render(request, 'blog-details.html')

    
def base(request):
    if request.method == 'POST':
        author_email = request.POST['news']
        con = news(email = author_email)
        con.save()
    return render(request, 'base.html')

def appoinment(request):
    return render(request, 'appoin.html')