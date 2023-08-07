from rest_framework import generics
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self,serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')\
        or None
        if content is None:
            content = title
        serializer.save(content=content)
product_List_Create_view = ProductListCreateAPIView.as_view()


class ProductDetaileAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
product_detail_view=ProductDetaileAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    '''
    Not Gonna Use

    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
product_list_view=ProductListAPIView.as_view()

# @api_view(["GET","POST"])
# def product_alt_view(request, pk=None, *args,**kwargs):
#     method = request.method
#     if method == 'GET':
#         if pk is not None:
            
#         # url_args??
#         # get request -> detail view
#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset,many=True).data
#         return Response(data)

#     if method == 'POST':
#         pass
#         serializer=ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             instance=serializer.save()
#             print(instance)
#             return Response(serializer.data)
#         return Response({"invalid":"Not good data"}, status=400)
    