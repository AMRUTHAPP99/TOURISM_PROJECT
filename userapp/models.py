from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class userregistrationdb(models.Model):
    uname = models.CharField(max_length=50, null=True, blank=True)
    uemail = models.EmailField(max_length=50, null=True, blank=True)
    umob = models.IntegerField(null=True, blank=True)
    upass = models.CharField(max_length=50, null=True, blank=True)

class Payment(models.Model):

    destname=models.CharField(max_length=100)

    due=models.CharField(max_length=100)
    locatn=models.IntegerField(null=True)
    dueprice = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)

class bookingdb(models.Model):
    destination_place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    joining_place=models.CharField(max_length=100)
    departure_date = models.CharField(max_length=100,null=True)

    mobile=models.IntegerField(null=True)
    members=models.CharField(max_length=100)
    package = models.IntegerField(null=True)

def __str__(self):
    return f"{self.user.username} - {self.destinationplace} {self.time}"


class feedbackdb(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    feedback=models.CharField(max_length=50,null=True,blank=True)

class history(models.Model):
    users= models.CharField(max_length=100,null=True,blank=True)
    des_place =models.CharField(max_length=100,null=True)
    rating=models.IntegerField(null=True)

class card(models.Model):
    Name= models.CharField(max_length=100, null=True, blank=True)
    Cnum = models.IntegerField(null=True, blank=True)
    Expdate = models.IntegerField(null=True, blank=True)
    Cvv = models.IntegerField(null=True, blank=True)


class checkout(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Bemail = models.EmailField(max_length=100, null=True, blank=True)
    Add = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.CharField(max_length=100, null=True, blank=True)
    Cname = models.CharField(max_length=100, null=True, blank=True)
    Cnum = models.IntegerField(null=True, blank=True)
    Expm = models.CharField(max_length=100, null=True, blank=True)
    Expyear = models.IntegerField(null=True, blank=True)
    Cvv = models.IntegerField(null=True, blank=True)

class contactdb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    msg=models.CharField(max_length=50,null=True,blank=True)
























