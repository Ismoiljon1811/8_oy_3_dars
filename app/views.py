from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Travel, Klass, Hotel
from .serializers import TravelSerializer, HotelSerializer, KlassSerializer


# Barcha ish bajarildi bu bitta voris olinayotgan class ham get, ham put, ham putch, ham delete qila oladi hamma shartlar bitta funksiyada qondirildi.


class TravelRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer



class KlassRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer


class HotelRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
































# class TravelDetailView(APIView):
#     def get(self, request: Request, pk = None):
#         if pk:
#             try:
#                 travel = Travel.objects.get(pk=pk)
#                 return Response(TravelSerializer(travel).data)
#             except:
#                 return Response({"message":"Bunday sayohat turi yo'q"})
#         travel = Travel.objects.all()
#         return Response({'travel':TravelSerializer(travel, many=True).data})
    
#     def post(self, request:Request):
#         serializer = TravelSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         travel = serializer.save()
#         return Response(TravelSerializer(travel).data)
    
#     def put(self, request: Request, pk=None):
#         if not pk:
#             return Response({"message":"Method PUT not allowed"})
#         try:
#             travel = Travel.objects.get(pk=pk)
#             serializer = TravelSerializer(instance=travel, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             updated_travel = serializer.save()
#             return Response(TravelSerializer(updated_travel).data)
#         except:
#             return Response({"message":"Bunday sayohat turi yo'q"})
    
#     def delete(self, request: Request, pk=None):
#         if not pk:
#             return Response({"message":"Method DELETE not allowed"})
#         try:
#             travel = Travel.objects.get(pk=pk)
#             travel.delete()
#             return Response({"message":"Success"})
#         except:
#             return Response({"message":"Bunday sayohat turi yo'q"})
    

# class KlassView(APIView):
#     def get(self, request, pk=None, *args, **kwargs):
#         if not pk:
#             transport = Klass.objects.all()
#             return Response({'transport':klassSerializer(transport, many=True).data})
#         try:
#             transport = Klass.objects.get(pk=pk)
#             serializer = klassSerializer(transport)
#             return Response(serializer.data)
#         except Klass.DoesNotExist:
#             return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)
        
#     def post(self, request:Request):
#         serializer = klassSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         transport = serializer.save()
#         return Response(klassSerializer(transport).data)
        
#     def put(self, request: Request, pk=None):
#         if not pk:
#             return Response({"message":"Method PUT not allowed"})
#         try:
#             transport = Klass.objects.get(pk=pk)
#             serializer = klassSerializer(instance=transport, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             updated_transport = serializer.save()
#             return Response(TravelSerializer(updated_transport).data)
#         except:
#             return Response({"message":"Bunday transport turi yo'q"})
        

#     def delete(self, request: Request, pk=None):
#         if not pk:
#             return Response({"message":"Method DELETE not allowed"})
#         try:
#             transport = Klass.objects.get(pk=pk)
#             transport.delete()
#             return Response({"message":"Success"})
#         except:
#             return Response({"message":"Bunday transport turi yo'q"})



# class HotelView(APIView):
#     def get(self, request, pk=None, *args, **kwargs):
#         if not pk:
#             mexmonxona = Hotel.objects.all()
#             return Response({'mexmonxona':HotelSerializer(mexmonxona, many=True).data})
#         try:
#             mexmonxona = Hotel.objects.get(pk=pk)
#             serializer = HotelSerializer(mexmonxona)
#             return Response(serializer.data)
#         except Hotel.DoesNotExist:
#             return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)
        
#     def post(self, request:Request):
#         serializer = HotelSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         mexmonxona = serializer.save()
#         return Response(TravelSerializer(mexmonxona).data)
        

#     def put(self, request: Request, pk=None):
#         if not pk:
#             return Response({"message":"Method PUT not allowed"})
#         try:
#             mexmonxona = Hotel.objects.get(pk=pk)
#             serializer = HotelSerializer(instance=mexmonxona, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             updated_mexmonxona = serializer.save()
#             return Response(TravelSerializer(updated_mexmonxona).data)
#         except:
#             return Response({"message":"Bunday mexmonxona turi yo'q"})
        

#     def delete(self, request: Request, pk=None):
#         if not pk:
#             return Response({"message":"Method DELETE not allowed"})
#         try:
#             mexmonxona = Hotel.objects.get(pk=pk)
#             mexmonxona.delete()
#             return Response({"message":"Success"})
#         except:
#             return Response({"message":"Bunday mexmonxona turi yo'q"})