from rest_framework.decorators import api_view
from rest_framework.response import Response
from. serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
def get_balance(requst):
    balance = Balance.objects.last()
    serialized_data = BalanceSerializer(balance).data
    return Response(serialized_data)



@api_view(['GET'])
def get_mytariff(requst):
    mytariff = MyTariff.objects.last()
    serialized_data = MyTariffSerializer(mytariff).data
    return Response(serialized_data)



@api_view(['GET'])
def get_bonus(requst):
    bonus = Bonus.objects.last()
    serialized_data = BonusSerializer(bonus).data
    return Response(serialized_data)



@api_view(['GET'])
def get_recomendate(requst):
    recomendate = Recomendate.objects.all()
    serialized_data = RecomendateSerializer(recomendate, many=True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_ad(requst):
    ad = Ad.objects.all()
    serialized_data = AdSerializer(ad, many=True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_unlim(requst):
    unlim = Unlim.objects.all()[:3]
    serialized_data = UnlimSerializer(unlim, many=True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_tariffs(requst):
    tariffs = Tariffs.objects.all()
    serialized_data = TariffsSerializer(tariffs, many=True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_packet(requst):
    packet = Packet.objects.all()
    serialized_data = PacketSerializer(packet, many=True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_minutsms(requst):
    minutsms = MinutSms.objects.all()
    serialized_data = MinutSmsSerializer(minutsms, many=True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_extraservice(requst):
    extraservice = Extraservice.objects.all()
    serialized_data = ExtraserviceSerializer(extraservice, many=True).data
    return Response(serialized_data)



@api_view(['GET'])
def get_ussd(requst):
    ussd = Ussd.objects.all()
    serialized_data = UssdSerializer(ussd, many=True).data
    return Response(serialized_data)




@api_view(['GET'])
def get_service(requst):
    service = Service.objects.all()
    serialized_data = ServiceSerializer(service, many=True).data
    return Response(serialized_data)



@api_view(['POST'])
def get_pay(requst):
    pay = Pay.objects.last()
    serialized_data = PaySerializer(pay).data
    return Response(serialized_data)



@api_view(['GET'])
def get_servicetype(requst):
    servicetype = ServiceType.objects.all()
    serialized_data = ServiceTypeSerializer(servicetype, many=True).data
    return Response(serialized_data)