# from re import A, L, T
# from tkinter import N, W
from .models import Customer
from .models import Wallet
from .models import Transaction
from .models import Reward
from .models import Receipt
from .models import Loan
from .models import Notifications
from .models import Card
from .models import Account
from .models import ThirdPartyAccount
from .models import Currency
from django.contrib import admin

# Register your models here.
# from.models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, ThirdPartyAccount, Transaction, Wallet

class CustormerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","age","email")
    search_fields=("first_name","last_name")
admin.site.register(Customer,CustormerAdmin)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Reward)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Notifications)
admin.site.register(Card)
admin.site.register(Account)
admin.site.register(ThirdPartyAccount)
admin.site.register(Currency)