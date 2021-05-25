from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date,datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Offer (models.Model):
    title = models.CharField(max_length=50)
    offer_amount = models.IntegerField()
    percentage = models.BooleanField(default=False)
    start_date =  models.DateField(default=datetime.now)
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length = 50,unique = True)
    description = models.TextField(max_length=250)
    offer=models.ForeignKey(Offer,on_delete=models.PROTECT,blank=True,null=True)
    
    def __str__(self):
        return self.name
class Image (models.Model):
    image = models.FileField(upload_to="media")

class Brand (models.Model):
    name = models.CharField(max_length = 50,unique = True)
    description = models.TextField(max_length = 250)
    logo = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True ,null=True)
    offer=models.ForeignKey(Offer,on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return self.name

class Review_and_rating(models.Model):
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    review = models.TextField(max_length=250)

COLOUR = (
		('black','Black'),
		('red','Red'),
		('brown','Brown'),
		('yellow','Yellow'),
		('blue','Blue'),
		('green','Green'),
		('orange','Orange'),
		('white','White'),
	)

class Colour(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Address (models.Model):
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name

class Seller (models.Model):
    name = models.CharField(max_length=50)
    number = PhoneNumberField()
    address = models.ForeignKey(Address,on_delete=models.PROTECT,blank=True,null=True)
    
    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    count = models.IntegerField()
    colours = models.ManyToManyField(Colour,blank=True,null=True)
    specifications = models.TextField(max_length=500)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,blank=True,null=True)
    reviews = models.OneToOneField(Review_and_rating, on_delete=models.CASCADE,blank=True,null=True)
    images = models.ManyToManyField(Image,blank=True)
    offer=models.ForeignKey(Offer,on_delete=models.PROTECT,blank=True,null=True)
    sold_out = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


PAYMENT_METHOD = (
		('cod','CASH ON DElIVERY'),
		('card','CARD PAYMENT'),
		('upi','UPI')
	)
ORDER_STATUS = (
		(0,'ORDER PLACED'),
        (1,'READY TO SHIP'),
		(2,'SHIPPED'),
		(3,'OUT FOR DELIVERY'),
        (4,'DELIVERED'),
        (5,'CANCELED'),
        (6,'RETURN REQUESTED'),
        (7,'RETURN COMPLETED')
	)
class Order (models.Model):
    order_id = models.CharField(max_length=50)
    placed_date = models.DateField(default=datetime.now)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address)
    order_status = models.CharField(max_length=50,choices= ORDER_STATUS,default="placed")
    payment_method = models.CharField(max_length=50,choices= PAYMENT_METHOD,default="card")
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id

    