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

def Login(request):
    if request.method == 'POST':
        username = request.POST['fl-name']
        password = request.POST['fl-pass']

        data = auth.authenticate(username=username,password=password)
        if data is not None :
            auth.login(request,data)
            return redirect('home')
        else:
            messages.info(request,'Incorrect Data')
            return redirect('login')
    else:
        return render(request, 'register.html')




def Signup(request):
    if request.method == 'POST':
        # take data from template
        username = request.POST['fs-name']
        #check for username
        if len(username) < 4 or check_username(username) == False:
            messages.info(request,'Enter Correct username')
            return redirect('signup')
        email = request.POST['fs-email']
        # ckeck valid email
        if check_email(email) == False :
            messages.info(request,'Enter Correct Email (example@gmail.com)')
            return redirect('signup')
        password = request.POST['fs-pass']
        password2 = request.POST['fs-passcon']
        if len(password) >= 8:
            # check if password match
            if password == password2:
                #check if username or email already exist
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email Already Used')
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request,'Username Already Used')
                    return redirect('signup')    
                # else will collect data and ckeck it before save
                else:
                    #check username is_valid
                    if username == '':
                        messages.info(request,'Input Your Username')
                        return redirect('signup')
                    #check email is_valid
                    elif email == '':
                        messages.info(request,'Input Your Email')
                        return redirect('signup')
                    #check password is_valid
                    elif password == '':
                        messages.info(request,'Input Your Password')
                        return redirect('signup')
                    #save data
                    else:
                        data = User.objects.create_user(username=username,email=email,password=password)
                        data.save()
                        messages.info(request,'Your accont created succesfully please login now')
                        return redirect('signup')
            # if passwords dont match
            else:
                messages.info(request,'Password Not The Same')
                return redirect('signup')
        else:
            messages.info(request,'Your password must contian at least 8 characters')
            return redirect('signup')
    else:
        return render(request,'register.html')
    
@login_required
def Logout(request):
    auth.logout(request)
    return redirect('home')