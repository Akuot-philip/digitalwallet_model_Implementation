from django.shortcuts import render
from . import models

from wallet.models import Customer
from .models import Customer
from .forms import CustomerRegistrationForm,CurrencyRegistrationForm, ReceiptRegistrationForm,TransactionRegistrationForm,WalletRegistrationForm,RewardRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,NotificationsRegistrationForm,CardRegistrationForm,AccountRegistrationForm,ThirdPartyRegistrationForm


# Create your views here.

def register_custormer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form =CustomerRegistrationForm()
    return render(request,"wallet/register_custormer.html",{"form": form} )

def list_customers(request):
    customers=models.Customer.objects.all()
    return render(request, "wallet/customers_list.html",
    {"customers":customers})

  
def register_currency(request):
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request,"wallet/currency_list.html",
    {"form": form}) 

def list_currency(request):
    currencys=models.Currency.objects.all()
    return render(request, "wallet/currency_list.html",
    { "currencys": currencys})    

def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request,"wallet/transaction_list.html",
    {"form": form}) 

def list_transaction(request):
    transactions=models.Transaction.objects.all()
    return render(request, "wallet/transaction_list.html",
    { "transactions": transactions})

    
# def register_wallet(request):
#     if request.method == "POST":
#         form = WalletRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = T()
#     return render(request,"wallet/transaction_list.html",
#     {"form": form}) 

# def list_transaction(request):
#     transactions=models.Transaction.objects.all()
#     return render(request, "wallet/transaction_list.html",
#     { "transactions": transactions})        













# def register_transaction(request):
#     form = TransactionRegistrationForm()
#     return render(request,"wallet/register_transaction.html",{"form": form})

def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form": form})

def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form": form})

def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form": form}) 

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form": form})

def register_notifications(request):
    form = NotificationsRegistrationForm()
    return render(request,"wallet/register_notifications.html",{"form": form})

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form": form})  

def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form": form})

def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form": form})

def list_customers(request):
    customers = models.Customer.objects.all()
    return render(request,"wallet/list_customers.html",
    {"customers": customers})




