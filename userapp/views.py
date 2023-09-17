from django.shortcuts import render,redirect
from userapp.models import userregistrationdb,bookingdb,feedbackdb,history,card,checkout,contactdb
from tourismapp.models import destinationdb,addproductdb
from django.contrib import messages
from django.utils.timezone import datetime
import random



# Create your views here.

def homepage_fn(req):
    return render(req,'homepage.html')
def registration_fn(req):
    return render(req,'loginpage.html')
def saveregistrationdata(req):
    if req.method=='POST':
        un=req.POST.get('username')
        ue=req.POST.get('email')
        um=req.POST.get('mobile')
        up=req.POST.get('password')

        obj=userregistrationdb(uname=un,uemail=ue,umob=um,upass=up)
        obj.save()
        return redirect(registration_fn)
def signup_fn(req):
    if req.method=='POST':
        uname=req.POST.get('u_name')
        upass=req.POST.get('u_pass')
        if userregistrationdb.objects.filter(uname=uname,upass=upass).exists():
            messages.success(req,"user login successfully")
            req.session['username']=uname
            req.session['password']=upass
            return redirect(homepage_fn)
        else:
            messages.error(req, "invalid user")
            return redirect(registration_fn)
    return redirect(registration_fn)


def userlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(homepage_fn)
def contactpage(req):
    return render(req,'contact.html')
def hotelbooking(req):
    return render(req,'hotel.html')
def destination_page(req):
    data=destinationdb.objects.all()
    return render(req,'destination.html',{'data':data})
def singledest_fn(req,dataid):
        dest = addproductdb.objects.get(id=dataid)
        return render(req, 'singledestination.html',{'dest':dest})

def booking_fn(req):
    data=bookingdb.objects.filter(name=req.session['username'])
    # des=destinationdb.objects.all()
    return render(req,'book_ticket.html',{'data':data})
def savebooking(req):
    if req.method == 'POST':

        n= req.POST.get('name')
        des= req.POST.get('dest')
        join = req.POST.get('joi')
        em= req.POST.get('email')
        ded=req.POST.get('dd')
        pa= req.POST.get('pack')
        m= req.POST.get('mob')
        me= req.POST.get('mem')
        obj=bookingdb(name=n,destination_place=des,joining_place=join,email=em,package=pa,mobile=m,members=me,departure_date=ded)
        obj.save()
        return redirect(paymentB)
def updatebooking(req):
    if req.method=='POST':
        n = req.POST.get('name')
        des = req.POST.get('dest')
        join = req.POST.get('joi')
        em = req.POST.get('email')
        ded = req.POST.get('dd')
        pa = req.POST.get('pack')
        m = req.POST.get('mob')
        me = req.POST.get('mem')

        bookingdb.objects.filter(name=req.session['username']).update(name=n,destination_place=des,joining_place=join,email=em,package=pa,mobile=m,members=me,departure_date=ded)
        return redirect(displaybook_fn)
def displaybook_fn(req):
    data=bookingdb.objects.filter(name=req.session['username'])
    return render(req,'displaybooking.html',{'data':data})
def deletebooking(req,dataid):
    data=bookingdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,'booking deleted successfully')
    return redirect(displaybook_fn)
def feedback_fn(req):
    return render(req,'text_feedback.html')
def savefeedback(req):
    if req.method=='POST':
        un=req.POST.get('username')
        fb=req.POST.get('feedbac')
        obj=feedbackdb(user=un,feedback=fb)
        obj.save()
        messages.success(req,"feedback saved successfully")
        return redirect(homepage_fn)
def contact_fn(req):
    return render(req,'contact.html')
def history_fn(req):
    data=bookingdb.objects.all()
    return render(req,'display_history.html',{'data':data})
# def savehistory(req):
#     if req.method=='POST':
#         us=req.POST.get('username')
#         dep=req.POST.get('')
#         ra=req.POST.get('')
#         obj=history(users=us,des_place=dep,rating=ra)
#         obj.save()
#         return redirect(homepage_fn)
def about_fn(req):
    return render(req,'about.html')
def cardpage(request):
    if request.method=="POST":
        x = request.POST.get('Name')
        y = request.POST.get('Cnum')
        a = request.POST.get('Expdata')
        b = request.POST.get('Cvv')

        obj = card(Name=x, Cnum=y, Expdate=a, Cvv=b)
        obj.save()

        return render(request,"invoice.html")

def save_Checkout(request):
    if request.method == "POST":

        x = request.POST.get('Name')
        y = request.POST.get('Bemail')
        a = request.POST.get('Add')
        b = request.POST.get('city')
        c = request.POST.get('State')
        d = request.POST.get('Pin')
        i = request.POST.get('Cname')
        e = request.POST.get('Cnum')
        f = request.POST.get('Expyear')
        g = request.POST.get('Expm')
        h = request.POST.get('Cvv')

        obj = checkout(Name=x, Bemail=y, Add=a, city=b, State=c, Pin=d, Cnum=e, Expyear=f, Expm=g, Cvv=h, Cname=i)
        obj.save()




        messages.success(request, "Payment done successfully!!")
        return redirect(invoice)

def invoice(request):
    invoice_number = random.randint(10000, 99999)

    context={
        'invoice_number':invoice_number
    }
    return render(request, "invoice.html", context=context)
def paymentB(request):
    data = bookingdb.objects.all()
    return render(request, "payment.html", {'data': data})
def chatbox(request):
    return render(request, "booking_success.html")

def editbooking(req,dataid):
    data=bookingdb.objects.get(id=dataid)
    return render(req,"editbooking.html",{"data":data})

def savecontactdata(req):
    if req.method=='POST':
        nm=req.POST.get('name')
        em=req.POST.get('email')
        ms=req.POST.get('message')
        obj=contactdb(name=nm,email=em,msg=ms)
        obj.save()
        return redirect(contactpage)

# def product_fn(req,dname):
#     pro_data=addproductdb.objects.all()
#     pro = addproductdb.objects.filter(name=dname)
#
#     return render(req,'destproduct.html',{'pro_data':pro_data,'pro':pro})

def deletehistory(req,dataid):
    data=bookingdb.objects.get(id=dataid)
    data.delete()
    messages.success(req,'booking deleted successfully')
    return redirect(history_fn)
def login_page(req):
    return render(req,"login.html")

def newfn(req,dname):
    pro_data=addproductdb.objects.all()
    pro=addproductdb.objects.filter(name=dname)
    return render(req,"destimages.html",{'pro_data':pro_data,'pro':pro})
def servicefn(req):
    return render(req,"services.html")

def search_results(request):
    if request.method=="GET":
        query=request.GET.get('query')
        brand_results=destinationdb.objects.filter(name__icontains=query)
        context ={
            'brand_results':brand_results
        }
        return render(request,'search_result.html',context)


















