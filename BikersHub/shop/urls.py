from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('products/',views.products,name='products'),

    path('customer_index/',views.customer_index,name='customer_index'),
    path('customer_about/',views.customer_about,name='customer_about'),
    path('customer_contact/',views.customer_contact,name='customer_contact'),
    path('customer_products/',views.customer_products,name='customer_products'),

    path('admin_index/',views.admin_index,name='admin_index'),
    path("show/",views.show_product,name="show"),
    path("add/",views.add_product,name="add"),
    path("delete/<i>/",views.delete_product),
    path("update/<i>/",views.update_product),
    path('show_contacts/', views.show_contacts, name='show_contacts'),
    path('delete_contact/<i>/', views.delete_contact, name='delete_contact'),
]