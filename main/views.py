from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    context = {
        'name': 'Joshua Montolalu',
        'class': 'PBP F',
        'products': Product.objects.all(),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("main:show_main")

    context = {
        "form": form,
    }

    return render(request, "create_product.html", context)

def show_xml(request):
    data = serializers.serialize("xml", Product.objects.all())
    return HttpResponse(data, content_type="application/xml")

def show_xml_by_id(request, id):
    data = serializers.serialize("xml", Product.objects.filter(pk=id))
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    data = serializers.serialize("json", Product.objects.all())
    return HttpResponse(data, content_type="application/json")

def show_json_by_id(request, id):
    data = serializers.serialize("json", Product.objects.filter(pk=id))
    return HttpResponse(data, content_type="application/json")