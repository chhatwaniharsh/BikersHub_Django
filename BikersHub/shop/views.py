from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Contact
from .forms import ProductForm, ContactForm
from django.contrib import messages


# Create your views here.
def index(request):
    template_name = 'base.html'
    context = {}
    return render(request, template_name, context)

def about(request):
    template_name = 'shop/about.html'
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = 'shop/contact.html'
    context = {}
    return render(request, template_name, context)

def products(request):
    template_name = 'shop/products.html'
    products = Product.objects.all()
    context = {"products": products}
    return render(request, template_name, context)

def customer_index(request):
    template_name = 'customer_panel/customer_base.html'
    context = {}
    return render(request, template_name, context)

def customer_about(request):
    template_name = 'customer_panel/about.html'
    context = {}
    return render(request, template_name, context)

def customer_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('customer_contact')

    form = ContactForm()
    return render(request, 'customer_panel/contact.html', {"form": form})

def customer_products(request):
    template_name = 'customer_panel/products.html'
    products = Product.objects.all()
    context = {"products": products}
    return render(request, template_name, context)

def admin_index(request):
    template_name = 'admin_panel/admin_base.html'
    context = {}
    return render(request, template_name, context)

def show_product(request):
    template_name = 'admin_panel/show_product.html'
    product_obj = Product.objects.all()
    context = {"product_obj": product_obj}
    return render(request, template_name, context)

def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'admin_panel/add_product.html'
    context = {"form": form}
    return render(request, template_name, context)

def delete_product(request,i):
    obj = Product.objects.get(id=i)
    obj.delete()
    return redirect('show')

def update_product(request,i):
    obj = Product.objects.get(id=i)
    form = ProductForm(instance=obj)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'admin_panel/update_product.html'
    context = {"form": form}
    return render(request, template_name, context)

def show_contacts(request):
    template_name = 'admin_panel/show_contact.html'
    contact_obj = Contact.objects.all()
    context = {"contact_obj": contact_obj}
    return render(request, template_name, context)

def delete_contact(request, i):
    obj = Contact.objects.get(id=i)
    obj.delete()
    return redirect('show_contacts')