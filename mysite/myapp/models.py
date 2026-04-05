from django.db import models

# Create your models here.
class Dreamreal(models.Model):
    website = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    online = models.ForeignKey('Online', default=1, on_delete=models.CASCADE, db_constraint=False)

    class Meta:
        db_table = "dreamreal"


class Online(models.Model):
    domain = models.CharField(max_length=30)

    class Meta:
        db_table = "online"

class Player(models.Model):
    user=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=128)
    name=models.CharField(max_length=50,blank=True)
    email=models.CharField(max_length=128,blank=True)
    win=models.IntegerField(default=0)
    lose=models.IntegerField(default=0)
    tie=models.IntegerField(default=0)

    class Meta:
        db_table='player'


# class Profile(models.Model):
#     name = models.CharField(max_length=50)
#     picture = models.ImageField(upload_to='static/picture')

#     class Meta:
#         db_table = "profile"
