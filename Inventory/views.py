from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GroceryItem
from .Serializers import GroceryItemSerializer
from django.shortcuts import render

# adding of grocery items
@api_view(['POST'])
def add_grocery_item(request):
    serializer = GroceryItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrive of grocery items
@api_view(['GET'])
def get_inventory(request):
    items = GroceryItem.objects.all()
    serializer = GroceryItemSerializer(items, many=True)
    return Response(serializer.data)

def display(request):
    items = GroceryItem.objects.all()
    return render(request, 'loadGrid.html', {'items': items})