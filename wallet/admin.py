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

class WalletAdmin(admin.ModelAdmin):
    list_display =("user_name", "phone_number","user_email","account_number", "account_name", 'balance')
    search_fields=("user_name", "phone_number", "user_email", "account_numberlast_name") 
admin.site.register(Wallet, WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display =("transaction", "wallet","transaction_amount","transaction_type","transaction_charge","transaction_type")
    search_fields=("transaction", "wallet","transaction_amount","transaction_type")
admin.site.register(Transaction,TransactionAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display =("country_of_origin", "symbol","amount")
    search_fields=("country_of_origin", "symbol","amount")
admin.site.register(Currency,CurrencyAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display =("account_number", "account_type", "balance", "name", "wallet")
    search_fields=("account_number", "account_type", "balance", "name", "wallet")
admin.site.register(Account,AccountAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display =("card_number","card_type","card_type","expiry_date","security_code")
    search_fields=("card_number","card_type","card_type","expiry_date","security_code")
admin.site.register(Card,CardAdmin)

class LoanAdmin(admin.ModelAdmin):
   list_display =("loan_id", "loan_type", "loan_balance", "amount", "interest","loan_term")
   search_fields=("loan_id", "loan_type", "loan_balance", "amount", "interest","loan_term")
admin.site.register(Loan,LoanAdmin)

class NotificationsAdmin(admin.ModelAdmin):
   list_display =("messages", "title", "status", "recepients","datetime")
   search_fields=("messages", "title", "status", "recepients","datetime")
admin.site.register(Notifications,NotificationsAdmin)



admin.site.register(Reward)
admin.site.register(Receipt)
admin.site.register(ThirdPartyAccount)
