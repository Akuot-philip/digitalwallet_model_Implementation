# from ast import walk
# from concurrent.futures.process import _python_exit
# from ctypes.wintypes import PINT
# from datetime import date, datetime
# from email import message
# from inspect import trace
# from locale import currency
# from multiprocessing.connection import wait
# from operator import mod
# from os import access
# from symtable import Symbol
# from telnetlib import STATUS
# from turtle import title
# from unicodedata import name
# from email.policy import default
# from tkinter import  TK   
# import re
# from tkinter import CASCADE
from django.db import models
# from pkg_resources import load_entry_point
# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.TextField(default='') 
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()

class Wallet(models.Model): 
    user_name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=13)
    user_email=models.EmailField()
    account_number=models.CharField(max_length=15)
    account_name=models.CharField(max_length=20)
    balance=models.IntegerField()
    amount=models.IntegerField()
    date_created=models.DateTimeField()
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='wallet_currency')
    status=models.CharField(max_length=20)
    pin=models.IntegerField()

class Transaction(models.Model):
    transaction=models.CharField(max_length=40,)
    wallet=models.ForeignKey(Wallet,on_delete=models. CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_amount=models.IntegerField()
    transaction_type=models.CharField(max_length=20)
    transaction_charge=models.IntegerField()
    datetime=models.DateTimeField()

class Reward(models.Model):
    points=models.BigIntegerField()
    date_of_reward=models.DateTimeField()
    transaction_amount=models.IntegerField()

class Receipt(models.Model):
    receipt_type=models.CharField(max_length=6)
    receipt_date=models.DateTimeField()
    transaction=models.IntegerField()
    total_amount=models.IntegerField()
    receipt_file=models.FileField()

class Loan(models.Model):
    loan_id=models.CharField(max_length=20)
    loan_type=models.CharField(max_length=20)
    amount=models.IntegerField()
    interest=models.IntegerField()
    loan_term=models.IntegerField()
    payment_due_date=models.DateTimeField()
    loan_balance=models.IntegerField()

class Notifications(models.Model):
    messages= models.TextField()
    title=models.CharField(max_length=20)
    status=models.CharField(max_length=20)   
    recepients=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="notifications_recepients")
    datetime=models.DateTimeField()

class Card(models.Model):
    card_number=models.IntegerField()
    card_name=models.CharField(max_length=20)
    expiry_date=models.DateTimeField()
    security_code=models.CharField(max_length=20)
    card_type=models.CharField(max_length=20)
    date_issue=models.DateTimeField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='card_wallet')
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='card_account')
    issuer=models.CharField(max_length=20)

class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20)
    balance = models.IntegerField()
    name=models.CharField(max_length=20)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Account_currency')

class ThirdPartyAccount(models.Model):
    account = models.ForeignKey('account',on_delete=models.CASCADE,related_name='account_third_party')
    name = models.CharField(max_length=20)
    transaction_cost = models.IntegerField()
    currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='third_party_currency')
    location=models.CharField(max_length=20)

class Currency(models.Model):
    country_of_origin = models.CharField(max_length=20)
    symbol=models.CharField(max_length=20)
    amount = models.IntegerField()    









    

