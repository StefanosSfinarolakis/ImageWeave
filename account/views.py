from django.shortcuts import render ,redirect

# Create your views here.

##lib##
from django.http import  HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

#if user is not loged in/ logged out
@login_required(login_url='signin')

#createrequest
def index(request):
    return render(request, 'index.html')


#den einai etoimo
@login_required(login_url='signin')
#accountsettings 
def settings(request):
   user_profile = Profile.objects.get(user=request.user)
   return render(request, 'setting.html', {'user_profile': user_profile})

#signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(usename=username, password=password)
                auth.login(request, user_login)
                #create a Profile object for the new user
                user_model = User.objects.get(username=user)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')   
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')
    

    #login
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('signin')    
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
#logout
def logout(request):
    auth.logout(request)
    return redirect('signin')

def startpage(request):
    return render(request , 'startpage.html')

def aboutus(request):
    return render(request, 'aboutus.html')