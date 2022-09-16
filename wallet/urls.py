from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns =[
    path("register/",views.register_custormer,name="registration"),
    path("currency/",views.register_currency,name="register_currency"),
    path("transaction/",views.register_transaction,name="register_transaction"),
    path("wallet/",views.register_wallet,name="register_wallet"),
    path("reward/",views.register_reward,name="register_reward"),
    path("receipt/",views.register_receipt,name="register_receipt"),
    path("loan/",views.register_loan,name="register_loan"),
    path("notifications/",views.register_notifications,name="register_notifications"),
    path("card/",views.register_card,name="register_card"),
    path("account/",views.register_account,name="register_account"),
    path("thirdparty/",views.register_thirdparty,name="register_thirdparty"),
    path("customers/", views.list_customers, name="customers_list"),
    path("currencys/", views.list_currency, name="currency_list"),
    path("transactions/", views.list_transaction, name="transaction_list"),











    # path("wallet/",include("wallet.urls")),
]