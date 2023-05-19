from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import utils as scrapper_utils
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def get_price(request):
    price_of_product = scrapper_utils.get_price_of_product("https://www.rcrsinnovations.in/prismatic-lithium-ion-cells.html")
    context = {
        "price": price_of_product
    }

    
    return Response(context)