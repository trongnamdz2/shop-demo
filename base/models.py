from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, name='notify', null=True)
    title = models.CharField(max_length=100, blank=True)
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images', null=True, blank=True)
    price = models.IntegerField()
    category = models.ManyToManyField(Category, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
class Images(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, null=True, name='img')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    
class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    cart = models.ManyToManyField(Item, blank=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
