from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date,datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length = 50,unique = True)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
class Image (models.Model):
    image = models.FileField(upload_to="media")

class Brand (models.Model):
    name = models.CharField(max_length = 50,unique = True)
    description = models.TextField(max_length = 250)
    logo = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True ,null=True)

    def __str__(self):
        return self.name

class Review_and_rating(models.Model):
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    review = models.TextField(max_length=250)

class Colour(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    count = models.IntegerField()
    colours = models.ManyToManyField(Colour)
    specifications = models.TextField(max_length=500)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    reviews = models.OneToOneField(Review_and_rating, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)
    sold_out = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Offer (models.Model):
    title = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)
    offer_amount = models.IntegerField()
    percentage = models.BooleanField(default=False)
    start_date =  models.DateField(default=datetime.now)
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Seller (models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    number = PhoneNumberField()
    product = models.ManyToManyField(Product)
    

class Address (models.Model):
    name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name

class Order (models.Model):
    order_id = models.CharField(max_length=50)
    placed_date = models.DateField(default=datetime.now)
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address)

    def __str__(self):
        return self.order_id

    