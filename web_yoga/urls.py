from django.urls import  path
from .views import index, about, product, pricing, yoga_online, contact #create_product

urlpatterns = [
path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('pricing/', pricing, name='pricing'),
    path('yoga_online/', yoga_online, name='yoga_online'),
    path('contact/', contact, name='contact'),
    #path('create_product/', create_product, name='create_product')
]