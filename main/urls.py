from django.urls import path
from.views import *

urlpatterns = [
    path('get-balance/', get_balance),
    path('get-mytariff/', get_mytariff),
    path('get-bonus/', get_bonus),
    path('get-recomendate/', get_recomendate),
    path('get-ad/',  get_ad),
    path('get-unlim/', get_unlim),
    path('get-tariffs/', get_tariffs),
    path('get-packet/', get_packet),
    path('get-minutsms/', get_minutsms),
    path('get-extraservice/', get_extraservice),
    path('get-ussd/', get_ussd),
    path('get-service/',  get_service),
    path('get-pay/', get_pay),
    path('get-servicetype/', get_servicetype),
]