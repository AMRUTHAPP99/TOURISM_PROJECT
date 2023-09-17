from django.shortcuts import render,redirect
from tourismapp.models import customerdb,destinationdb,addproductdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from userapp.models import feedbackdb,bookingdb



# Create your views here.
def index_fun(req):
    return render(req,'index.html')
def add_customerfn(req):
    return render(req,"addcustomers.html")
def savedata_fn(req):
    if req.method=='POST':
        cn=req.POST.get('c_name')
        im=req.FILES['image']
        mem=req.POST.get('member')
        mob_no=req.POST.get('mobile')
        add=req.POST.get('addresses')
        loc=req.POST.get('loctn')
        obj=customerdb(cname=cn,cimage=im,members=mem,mobileno=mob_no,address=add,location=loc)
        obj.save()
        return redirect(add_customerfn)

def displaypage_fn(req):
    data=customerdb.objects.all()
    return render(req,'displaypage.html',{'data':data})
def editcustomer_fn(req,dataid):
    data=customerdb.objects.get(id=dataid)
    return render(req,"editcustomer.html",{"data":data})
def updatetourism(req,dataid):
    if req.method=='POST':
        cn = req.POST.get('c_name')
        mem = req.POST.get('member')
        mob_no = req.POST.get('mobile')
        add = req.POST.get('addresses')
        loc = req.POST.get('loctn')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = customerdb.objects.get(id=dataid).cimage
        customerdb.objects.filter(id=dataid).update(cname=cn,cimage=file,members=mem,mobileno=mob_no,address=add,location=loc)
        return redirect(displaypage_fn)
def deletecustomer(req,dataid):
    data=customerdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypage_fn)

def login_page(req):
    return render(req,"login.html")


def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "login successfully")
                request.session['username'] = uname
                request.session['password'] = pwd
                return redirect(index_fun)
            else:
                messages.error(request,"invalid user")
                return redirect(login_page)
        else:
            messages.error(request,"invalid user")
            return redirect(login_page)

def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(login_page)

def add_destination(req):
    return render(req,"adddestination.html")
def savedestination_fn(req):
    if req.method=='POST':
        nm=req.POST.get('dname')
        files=req.FILES.getlist('files')
        de=req.POST.get('des')
        locn=req.POST.get('loct')
        pri=req.POST.get('price')
        for i in files:
            obj=destinationdb(name=nm,img=i,price=pri,descrip=de,lo=locn)
            obj.save()
            messages.success(req, 'category added succesfully')

        return redirect(add_destination)
def displaydest_fn(req):
    data=destinationdb.objects.all()
    return render(req,'displaydestination.html',{'data':data})
def editdest_fn(req,dataid):
    data=destinationdb.objects.get(id=dataid)
    return render(req,"editdestination.html",{"data":data})
def updatedestination(req,dataid):
    if req.method=='POST':
        nm = req.POST.get('dname')
        de = req.POST.get('des')
        locn = req.POST.get('loct')
        pri = req.POST.get('price')
        try:
            imgs = req.FILES['images']
            fs = FileSystemStorage()
            file = fs.save(imgs.name, imgs)
        except MultiValueDictKeyError:
            file = destinationdb.objects.get(id=dataid).img
        destinationdb.objects.filter(id=dataid).update(name=nm,img=file,price=pri,descrip=de,lo=locn)
        return redirect(displaydest_fn)
def deletedestination(req,dataid):
    data=destinationdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydest_fn)
def viewfeedback(req):
    data=feedbackdb.objects.all()
    return render(req,'display_feedback.html',{'data':data})
def user_details(req):
    return render(req,"view_booking.html")
def viewbooking(req):
    data=bookingdb.objects.all()
    return render(req,'view_booking.html',{'data':data})

def addproduct_fn(req):
    category = destinationdb.objects.all()
    return render(req,'addproduct.html',{'category':category})

def save_addproductdata(req):
    if req.method=='POST':
        c_name=req.POST.get('pcname')
        p_name=req.POST.get('pr_name')
        price=req.POST.get('pr_price')
        description=req.POST.get('description')
        pimg=req.FILES['p_image']
        obj=addproductdb(name=c_name,pn=p_name,pr=price,ds=description,pi=pimg)
        obj.save()
        return redirect(addproduct_fn)

def displayproduct_fn(req):
    product=addproductdb.objects.all()
    return render(req,'displayproduct.html',{'product':product})

def editaddproduct_fn(req,productid):
    product=addproductdb.objects.get(id=productid)
    return render(req,'editproduct.html',{'product':product})

def updateaddproduct(req,productid):
    if req.method=='POST':
        c_name = req.POST.get('pcname')
        p_name = req.POST.get('pr_name')
        price = req.POST.get('pr_price')
        description = req.POST.get('description')

        try:
            pimg = req.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(pimg.name,pimg)
        except MultiValueDictKeyError:
            file = addproductdb.objects.get(id=productid).pi
        addproductdb.objects.filter(id=productid).update(name=c_name,pn=p_name,pr=price,ds=description,pi=file)
        return redirect(displayproduct_fn)

def deleteaddproduct(req,productid):
    data=addproductdb.objects.filter(id=productid)
    data.delete()
    return redirect(displayproduct_fn)
def deletefeed(req,dataid):
    data=feedbackdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewfeedback)








