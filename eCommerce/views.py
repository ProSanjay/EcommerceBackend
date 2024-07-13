from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .product import product

# Create your views here.

@api_view(['GET'])
def demo(request):
    return Response("successfulyy")

@api_view(['GET'])
def getProduct(request):
    return Response(product)
