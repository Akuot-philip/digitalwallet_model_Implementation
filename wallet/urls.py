from xml.etree.ElementInclude import include
from django.urls import path
from.views import register_card, register_custormer,register_currency, register_notifications,register_transaction, register_wallet,register_reward,register_receipt,register_loan,register_card,register_account,register_thirdparty

urlpatterns =[
    path("register/",register_custormer,name="registration"),
    path("currency/",register_currency,name="register_currency"),
    path("transaction/",register_transaction,name="register_transaction"),
    path("wallet/",register_wallet,name="register_wallet"),
    path("reward/",register_reward,name="register_reward"),
    path("receipt/",register_receipt,name="register_receipt"),
    path("loan/",register_loan,name="register_loan"),
    path("notifications/",register_notifications,name="register_notifications"),
    path("card/",register_card,name="register_card"),
    path("account/",register_account,name="register_account"),
    path("thirdparty/",register_thirdparty,name="register_thirdparty"),







    # path("wallet/",include("wallet.urls")),
]