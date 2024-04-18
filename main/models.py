from django.db import models



class Balance(models.Model):
    balance = models.CharField(max_length=100)



class MyTariff(models.Model):
    name = models.CharField(max_length=100)
    gb = models.IntegerField()
    minute = models.CharField(max_length=100)
    sms = models.IntegerField()


class Bonus(models.Model):
    name = models.CharField(max_length=100)
    coin = models.IntegerField()



class Recomendate(models.Model):
    name = models.CharField(max_length=100)



class Ad(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=100)



class Unlim(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField()



class Tariffs(models.Model):
    name = models.CharField(max_length=100)
    mb = models.IntegerField()
    sms = models.IntegerField()



class Packet(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()



class MinutSms(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()



class ExtraService(models.Model):
    name =  models.CharField(max_length=100)
    price = models.IntegerField()



class Ussd(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)



class Service(models.Model):
    tariffs = models.ManyToManyField('Tariffs')
    packet = models.ManyToManyField('Packet')
    unlim = models.ManyToManyField('Unlim')
    minutsms = models.ManyToManyField('MinutSms')
    extraservice = models.ManyToManyField('ExtraService')
    rouming = models.BooleanField(default=False)
    ussd = models.ManyToManyField('Ussd')
    mobicinema = models.BooleanField(default=False)



class Pay(models.Model):
    title = models.CharField(max_length=25)
    phone = models.CharField(max_length=20, unique=True)



class ServiceType(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=25)
    