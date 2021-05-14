from django.shortcuts import render,redirect
from .models import Donator
from django.contrib import messages


# Create your views here.
def feeddata(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        adhar_no = request.POST['adhar_no']
        email = request.POST['email']

        age = request.POST['age']
        sex = request.POST['sex']


        address=request.POST['address']
        district=request.POST['district']


        pin=request.POST['pin']
        mob=request.POST['mob']

        blood_grp = request.POST['blood_grp']
        weight = request.POST['weight']

        diabetic = request.POST['diabetic']
        disease = request.POST['disease']


        donator = Donator(first_name=first_name, last_name=last_name,email=email,username=request.user.username,adhar_no=adhar_no,dob='',age=age,sex=sex,address=address,district=district, mob=mob, pin=pin,blood_grp=blood_grp,weight=weight,diabetic=diabetic,disease=disease)

        donator.save()
        return redirect('/volunteers/show_info')

    else:
        return render(request,'feed_data.html')




'''def fetch_blood_group(request):
    if request.method=="POST":
        blood_group = request.POST['blood_group']
        unique_number= request.POST['unique_number']
        l = [101, 1011, 10111, 101111, 1011111]
        list_of_don_obj=[]
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

                return render(request,'show_donors.html',{'donors':list_of_don_obj})
            else:
                messages.info(request, 'Sorry!No Donor availabe for this blood group')
                return redirect('/volunteers/fetch_blood_group')

        else:
            messages.info(request, 'You dont have access to this data')
            return redirect('/')



    else:
        return redirect('')

'''



def show_info(request):

    for don in Donator.objects.all():
        if request.user.username==don.username:

            return render(request,'show_info.html',{'don':don})