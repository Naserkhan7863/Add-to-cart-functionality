from django.shortcuts import render,redirect
from adminapp.models import UserDetailsModel, UserEnquiryModel
from django.db.models import Q

# Create your views here.

def admin_home(request):
    return render(request,'admin/admin-home.html')
def admin_add_user(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        contact = request.POST.get('contact')
        subject = request.POST.get('subject')
        UserDetailsModel.objects.create(name=name,email=email,contact=contact,subject=subject)
    return render(request,'admin/admin-add-user.html')
def admin_view_user(request):
    user= UserDetailsModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        user = UserDetailsModel.objects.filter(Q(user_id__icontains=search) | Q(name__icontains=search) | Q(subject__icontains=search)  | Q(contact__icontains=search))
    return render(request,'admin/admin-view-user.html',{'k':user})

def admin_view_queries(request):
    data= UserEnquiryModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        data = UserEnquiryModel.objects.filter(Q(user_id__icontains=search) | Q(name__icontains=search) | Q(subject__icontains=search)  | Q(contact__icontains=search))
    return render(request,'admin/admin-view-queries.html',{'k':data})

def delete_queries(request,id):
    w = UserEnquiryModel.objects.filter(user_id=id)
    w.delete()
    return redirect('admin_view_queries')

def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('email')
        password = request.POST.get('password')
        if name =='admin' and password =='admin':
            return redirect('admin_home')
        elif name =='venkat' and password =='venkat':
            return redirect('admin_home')
        else:
           pass
    return render(request,'admin/admin-login.html')