from django.shortcuts import render ,HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from home.models import Userdata
from django.contrib.auth import logout

def index(request):
    return render(request,"index.html")

def admission(request):
    return render(request,"admission.html")

def technicalclubs(request):
    return render(request,"technicalclubs.html")
    
def nontechnicalclubs(request):
    return render(request,"nontechnicalclubs.html")    

def signup(request):
    if request.method == "POST":
       username = request.POST['form3Example1cg']
       email = request.POST['form3Example3cg']
       password = request.POST['form3Example4cg']
       conf_pass = request.POST['form3Example4cdg']
       if Userdata.objects.filter(username=username).exists():
           messages.error(request, 'This username is already taken')
           return redirect('signup')
       elif Userdata.objects.filter(email=email).exists():
           messages.error(request, 'This email is already taken')
           return redirect('signup')
       elif(password != conf_pass):
           messages.error(request, 'Please enter same password')
           return redirect('signup')
       else:
           students = Userdata(username=username, email=email, password=password, conf_pass=conf_pass)
           students.save()
           return redirect('login')
    return render(request, 'signup.html')

def login(request): 
    if request.method == "POST":
        email = request.POST['form3Example3']
        passw = request.POST['form3Example4']
        if Userdata.objects.filter(email=email).exists():
            if Userdata.objects.filter(password=passw).exists():
                return redirect('home')
            else:
                messages.error(request, 'Incorrect password')
                return redirect('login')
        else:
            messages.error(request, 'Incorrect email')
            return redirect('login')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)   
    return redirect('login')
    
