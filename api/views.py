from django.shortcuts import render
from api.serializers import ProductSerializer
from product.models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ProductsView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def single_product(self, id_arg):
        try:
            queryset = Product.objects.get(id=id_arg)
            return queryset
        except Product.DoesNotExist:
            return None

    def get(self, request, id_arg):
        queryset = self.single_product(id_arg)
        if queryset:
            serializer = ProductSerializer(queryset)
            return Response(serializer.data)
        else:
            # Handle response for an id that is not an existing product
            return Response(
                {"msg" : f"Product with the id:{id_arg} does not exist"},
                status.HTTP_400_BAD_REQUEST
            )
