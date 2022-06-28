from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator,\
    RegexValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=CASCADE)
    bio = models.TextField(null=True)
    disease = models.TextField(null=True)
    age = models.IntegerField(validators = [MinValueValidator(18),MaxValueValidator(100)],null=True)
    full_address = models.TextField(null=True)
    contact_no = models.CharField(max_length=20,validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],null=True)
    def __str__(self):
        return self.user
    
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True) 
    medicine_img = models.ImageField(upload_to="medicine//")
    price = models.FloatField(default=0.0,validators=[MinValueValidator(0.0)])
    mfg_date = models.DateField(null=True,blank=True)
    exp_date = models.DateField(null=True,blank=True) 
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    user = models.ForeignKey(to=User,on_delete=CASCADE,null=True)
    medicine = models.ForeignKey(to=Medicine,on_delete=CASCADE)
    quantity = models.IntegerField(default=1,validators=[MinValueValidator(0)])
    total_price = models.FloatField(null=True)
    delivery_status = models.CharField(max_length=50,default='ordered',choices=(('ordered','Ordered'),('ordered','Ordered'),('shipping','Shipping'),('delivered','Delivered'),))    
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s(%s)" % (self.medicine,self.user)
    
         
class Review(models.Model):
    orders = models.ForeignKey(to=Orders,on_delete=CASCADE,null=True)
    rating = models.IntegerField(default=1,choices=((1,"One Rating"),(2,"Two Rating"),(3,"Three Rating"),(4,"Four Rating"),(5,"Five Rating"),))
    comment = models.TextField(null=True,blank=True)
    def __str__(self):
        return "%s(%s)" % (self.orders,self.rating)
    