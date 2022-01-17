from django.http import HttpRequest
from django_filters import filters
from rest_framework import pagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import BrandSerializer, CapsSerializer, CapCreateValidateSerializer
from .models import Brand, Cap
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CapListAPIView(ListAPIView):
    queryset = Cap.objects.all()
    serializer_class = CapsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['brand','size']
    search_fields = ['name']



class CapDetailAPIView(RetrieveAPIView):
    queryset = Cap.objects.all()
    serializer_class = CapsSerializer
    lookup_field = 'id'





# @api_view(['GET', 'DELETE', 'PUT'])
# def cap_detail_view(request: HttpRequest, id):
#     try:
#         cap = Cap.objects.get(id=id)
#     except Cap.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND,
#             data={
#                 "ERROR": "Cap does not exist!"
#             }
#             )
#     if request.method == 'GET':
#         serializer = CapsSerializer(cap, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'PUT':
#         serializer = CapCreateValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
#         cap.name = request.data['name']
#         cap.imege = request.data['imege']
#         cap.description = request.data['description']
#         cap.price = request.data['price']
#         cap.brand_id = request.data['brand']
#         cap.size.set(request.data['size'])
#         cap.save()
#         return Response(data={'message': 'cap updated'})
#     elif request.method == 'DELETE':
#         cap.delete()
#         return Response(data={'message': 'cap deleted'})


# @api_view(['GET', 'POST'])
# def caps_list_view(request: HttpRequest):
#     if request.user and request.user.is_authenticated:
#         cap = Cap.objects.all()
#         serializer = CapsSerializer(cap, many=True)
#         return Response(data=serializer.data)


#     elif request.method == 'POST':
#         serializer = CapCreateValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
#         name = request.data['name']
#         imege = request.data['imege']
#         description = request.data['description']
#         price = request.data['price']
#         brand = request.data['brand']
#         size = request.data['size']


#         product = Cap.objects.create(
#             name=name,
#             imege=imege,
#             description=description,
#             price=price,
#             brand_id=brand,
#         )
#         product.save()
#         product.size.set(size)
#         product.save()
#         return Response("Cap succesfully created!")