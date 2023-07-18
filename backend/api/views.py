# from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from products.models import Product
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):

    # if request.method!="POST":
    #     return Response({"detailed":"GET NOT ALLOWED"},status=405)

    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price
        # data = model_to_dict(model_data, fields=['id','title', 'content', 'price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data, headers = {'content-type':'application/json'})