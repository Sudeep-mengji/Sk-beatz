from django.shortcuts import render,redirect
from .models import contact,homecontact,admin_home,admin_home2,admin_about,Music
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    msg=""
    if request.method=="POST":
        name=request.POST["name"]
        mail=request.POST["email"]
        if homecontact.objects.filter(name=name,mail=mail).exists():
            msg="!!Data already exists!!"
        else:
            data=homecontact(name=name,mail=mail)
            data.save()
            msg="!!Data saved successfully!!"
    photo=admin_home.objects.all()
    photo2=admin_home2.objects.all()
    return render(request,'pages/index.html',{'msg':msg,'photo':photo,'photo2':photo2})

def about(request):
    data_about=admin_about.objects.all()
    return render(request,"pages/about.html",{'data_about':data_about})

def contactus(request):
    msg=""
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['textbox']
        if contact.objects.filter(name=name,email=email,subject=subject,message=message).exists():
            msg="Data already exists"
        else:
            data=contact(name=name,email=email,subject=subject,message=message)
            data.save()
            msg="Data sent succesfully"
    return render(request,"pages/contact.html",{'msg':msg})


def work(request):
    msg=""
    songs = Music.objects.all()
    if request.method=="POST":
        search=request.POST['search']
        if search!="":
            if Music.objects.filter(title__icontains=search).exists():
                songs=Music.objects.filter(title__icontains=search)
                
            else:
                msg="!! Data not found !!"
                songs=""
    return render(request,"pages/work.html",{'songs':songs,'msg':msg})


# Admin views

def login_page(request):
    if request.method=="POST":
        username=request.POST["username"]
        phone=request.POST["phone"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("admin_home_page")
    return render(request,"admin pages/login.html")

def logout_btn(request):
    logout(request)
    return redirect('homepage')


def admin_home_page(request):
    msg=""
    if request.method=="POST":
        file1=request.FILES["file"]
        document=admin_home(image=file1)
        document.save()
        msg="File uploaded"
    data=admin_home.objects.all()
    data2=admin_home2.objects.all()
    return render(request,'admin pages/home_page.html',{"msg":msg,'data':data,'data2':data2})



def home_page2(request):
    if request.method=="POST":
        img=request.FILES["file1"]
        link=request.POST["link"]
        document=admin_home2(img=img,link=link)
        document.save()
        return redirect('admin_home_page')
    data=admin_home.objects.all()
    data2=admin_home2.objects.all()
    return render(request,'admin pages/home_page.html',{'data':data,'data2':data2})


def delete_img(request):
    if request.method=="POST":
        id=request.POST["img"]
        data=admin_home.objects.filter(id=id)
        data.delete()
        return redirect('admin_home_page')
    return render(request,'admin pages/home_page.html')

def delete_img2(request):
    if request.method=="POST":
        id=request.POST["img"]
        data=admin_home2.objects.filter(id=id)
        data.delete()
        return redirect('admin_home_page')
    return render(request,'admin pages/home_page.html')


def about_page(request):
    msg=""
    if request.method=="POST":
        file1=request.FILES["file"]
        document=admin_about(image=file1)
        document.save()
        msg="File uploaded"
    data_about=admin_about.objects.all()
    return render(request,'admin pages/about_page.html',{'data_about':data_about,'msg':msg})

def delete_about(request):
    if request.method=="POST":
        id=request.POST["img"]
        data=admin_about.objects.filter(id=id)
        data.delete()
        return redirect('about_page')
    return render(request,'admin pages/home_page.html')

def work_page(request):
    msg=""
    if request.method=="POST":
        title=request.POST["title"]
        artist=request.POST["artist"]
        audio_file=request.FILES["audio"]
        album_art=request.FILES["album_art"]
        document=Music(title=title,artist=artist,audio_file=audio_file,album_art=album_art)
        document.save()
        msg="File uploaded"
    data_work=Music.objects.all()
    return render(request,'admin pages/work_page.html',{'msg':msg,'data_work':data_work})


def delete_work(request):
    if request.method=="POST":
        id=request.POST["id"]
        data=Music.objects.filter(id=id)
        data.delete()
        return redirect('work_page')
    return render(request,'admin pages/work_page.html')


def contact_page(request):
    contact_list=contact.objects.all()
    return render(request,'admin pages/contact_page.html',{'contact_list':contact_list})

def delete_contact(request):
    msg=''
    if request.method=="POST":
        id=request.POST['contactid']
        data=contact.objects.filter(id=id)
        data.delete()
        msg="!! Record deleted successfully !!"
        return redirect('contact_page')
    return render(request,'admin pages/contact_page.html',{'msg':msg})

# new code

def music_list(request):
    songs = Music.objects.all()
    return render(request, 'pages/work.html', {'songs': songs})

