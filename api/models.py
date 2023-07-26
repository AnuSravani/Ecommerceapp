from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Categories(models.Model):
    title=models.CharField(max_length=250)
    is_available=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title
    

class Products(models.Model):
    Products_options = (
    ('laptop', 'Laptop'),
    ('Tablet', 'Tablet'),
    ('earphone', 'Ear Phone'),
    ('chair', 'chair'),
    ('chain', 'chain'),
    )
    

    name=models.CharField(max_length=250)
    product_tag=models.CharField(max_length=200,unique=True)
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    product=models.CharField(choices=Products_options, max_length=100)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name="category")
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.CharField(max_length=250)
    is_active=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    

    def is_registered_before_two_months(self):
        two_months_ago = timezone.now() - timezone.timedelta(days=60)
        if self.created_date == None:
            return False
        return self.created_date < two_months_ago

    def save(self, *args, **kwargs):
        if self.is_registered_before_two_months():
            self.is_active = False
        super(Products, self).save(*args, **kwargs)

    class Meta:
        ordering=["-created_date"]

    def __str__(self) -> str:
        return self.name 
    
