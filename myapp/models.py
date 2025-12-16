from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_worker = models.BooleanField(default=False)
    def __str__(self):
        _sentence = "worker" if self.is_worker else "client"
        return ("{}: {}".format(self.user,_sentence ))



class Order(models.Model):
    client = models.CharField(max_length=15)
    # client_type = models.ForeignKey(Client,on_delete=models.CASCADE)
    number = models.IntegerField(primary_key=True)
    time = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    delivered = models.BooleanField(default=False)
    adress =  models.CharField(max_length=200, null=True)
    def __str__(self):
        _delivered_sentence = "Delivered" if self.delivered else "Not delivered"
        return ("{} |  {} ({})".format(self.number, self.name.upper(), _delivered_sentence ))

class Product(models.Model):
    name = models.CharField(max_length=20)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        _delivered_sentence = "Delivered" if self.order.delivered else "Not delivered"
        return ("{} | from  {} ({})".format(self.name.upper(), self.order.name, _delivered_sentence ))
