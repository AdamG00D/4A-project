from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def check_email(email):
    
    x=0
    for char in email:
        x+=1
        if char == '@':
            break

    domain = email[x:]
    # in the same dir 
    domains = open('registration\\domains.txt','r')


    if domain not in domains.read():
        return False
        

def check_username(name):
    file = open('registration\\allowed.txt','r')
    
    chars = file.read()
    for char in name:
        if char not in chars:
            return False

def home(request):
    return render(request,'index.html')
    

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST' and request.POST['f-type'] == 'signup':
        # take data from template
        username = request.POST['fs-name']
        #check for username
        if len(username) < 4 or check_username(username) == False:
            messages.info(request,'Enter Correct username')
            return redirect('register')
        email = request.POST['fs-email']
        # ckeck valid email
        if check_email(email) == False :
            messages.info(request,'Enter Correct Email (example@gmail.com)')
            return redirect('register')
        password = request.POST['fs-pass']
        password2 = request.POST['fs-passcon']
        if len(password) >= 8:
            # check if password match
            if password == password2:
                #check if username or email already exist
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email Already Used')
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(request,'Username Already Used')
                    return redirect('register')    
                # else will collect data and ckeck it before save
                else:
                    #check username is_valid
                    if username == '':
                        messages.info(request,'Input Your Username')
                        return redirect('register')
                    #check email is_valid
                    elif email == '':
                        messages.info(request,'Input Your Email')
                        return redirect('register')
                    #check password is_valid
                    elif password == '':
                        messages.info(request,'Input Your Password')
                        return redirect('register')
                    #save data
                    else:
                        data = User.objects.create_user(username=username,email=email,password=password)
                        data.save()
                        data = auth.authenticate(username=username,password=password)
                        if data is not None :
                            auth.login(request,data)
                            return redirect('home')
                        else:
                            messages.info(request,'Error')
                            return redirect('register')
            # if passwords dont match
            else:
                messages.info(request,'Password Not The Same')
                return redirect('register')
        else:
            messages.info(request,'Your password must contian at least 8 characters')
            return redirect('register')
    # Login FUNC
    elif request.method == 'POST' and request.POST['f-type'] == 'login':
        username = request.POST['fl-name']
        password = request.POST['fl-pass']

        data = auth.authenticate(username=username,password=password)
        if data is not None :
            auth.login(request,data)
            return redirect('home')
        else:
            messages.info(request,'Incorrect Data')
            return redirect('register')
    else:
        return render(request,'register.html')



@login_required
def Logout(request):
    auth.logout(request)
    return redirect('home')