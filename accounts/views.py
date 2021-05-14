from django.shortcuts import render,redirect

from django.contrib.auth.models import User, auth
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib import messages
from volunteers.models import Donator
from django.conf import settings
from django.core.mail import send_mail
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')

                return redirect('register')


            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email  taken')

                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save()
                auth.login(request,user)

                return redirect('/accounts/login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')


    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            for don in Donator.objects.all():
                if user.username==don.username:
                    return redirect('/volunteers/show_info')
            else:
                return redirect('/volunteers/feeddata')

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')


    else:
        return render(request, 'login.html')

def Org_Register(request):
    #l=[101,1011,10111,101111,1011111]
    '''if request.method == "POST":
        Hospital_name = request.POST['Hospital_name']
        unique_number = request.POST['unique_number']
        Contact_number = request.POST['Contact_number']

        if(unique_number in l):
            return redirect(request,'/volunteers/fetch_blood_group')
        else:
            messages.info(request,'Wrong credentials')
            return render(request,'organisation_reg.html')
    else:
        return render(request,'organisation_reg.html')'''
    l = ['101', '1011', '10111']
    if request.method == "POST":
        blood_group = request.POST['blood_group']
        unique_number = request.POST['unique_number']

        list_of_don_obj = []
        for p in Donator.objects.raw("SELECT * from volunteers_donator where blood_grp = '{}' ".format(blood_group)):
            list_of_don_obj.append(p)
        if (unique_number in l):
            if list_of_don_obj:
                subject = 'Regarding Plasma Donation'
                message = f'Dear{p.username},' \
                          f'Our hospital needs {p.blood_grp} plasma urgently and we were glad to know you are willing for the same. So please come asap for this noble purpose'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [don.email for don in list_of_don_obj]
                send_mail(subject, message, email_from, recipient_list)

                return render(request, 'show_donors.html', {'donors': list_of_don_obj})
            else:
                messages.info(request, 'Sorry!No Donor availabe for this blood group')
                return redirect('/accounts/Org_Register')

        else:
            messages.info(request, 'You dont have access to this data')
            return redirect('/accounts/Org_Register')
    else:
        return render(request, 'organisation_reg.html')




def logout(request):
	auth.logout(request)
	return redirect('/')
