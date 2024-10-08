from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hotels, User
from .serializers import HotelsSerializer
import random

# Create your views here.



class HotelViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Hotels.objects.all()
        serializer = HotelsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        serializer = HotelsSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def retrieve(self, request, pk=None):
        product = Hotels.objects.get(id = pk)
        serializer = HotelsSerializer(product)
        return Response(serializer.data)


    def update(self, request, pk=None):
        product = Hotels.objects.get(id=pk)
        serializer = HotelsSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

    def destroy(self, request, pk=None):
        product = Hotels.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        if users:
            user = random.choice(users)
            return Response(
                {'id': user.id},
                status.HTTP_200_OK
                )
        else:
            return Response(
                {'message': 'No users available'}, 
                status=status.HTTP_404_NOT_FOUND
                )