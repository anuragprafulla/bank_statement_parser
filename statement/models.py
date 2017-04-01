from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    account_no = models.CharField(max_length=25)
    branch = models.CharField(max_length=25)
    ifsc = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User)
    txn_name = models.CharField(max_length=50)
    txn_date = models.DateField()
    value_date = models.DateField()
    description = models.CharField(max_length=256)
    debit = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    balance = models.IntegerField()

    def __str__(self):
        return self.txn_name

class Statement(models.Model):
    statement = models.FileField(upload_to='uploads/') 
   
    def __str__(self):
        return self.statement
