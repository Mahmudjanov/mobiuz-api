from rest_framework import serializers
from.models import *




class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = "__all__"



class MyTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTariff
        fields = "__all__"


    
class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = "__all__"



class RecomendateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendate
        fields = "__all__"



class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"



class UnlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unlim
        fields = "__all__"        



class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariffs
        fields = "__all__"



class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = "__all__"



class MinutSmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinutSms
        fields = "__all__"



class ExtraServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraService
        fields = "__all__"



class UssdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ussd
        fields = "__all__"




class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"



class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = "__all__"



class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"