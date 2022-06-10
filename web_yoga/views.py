from django.shortcuts import render

# Create your views here.
def index(request):
    # products = Product.objects.all()[:4]
    # coaches = Coach.objects.all()[:4]
    # context = {
    #     'products': products,
    #     'coaches': coaches
    # }
    return render(request, 'web_yoga/index.html')

def about(request):
    return render(request, 'web_yoga/about.html')

def product(request):
    return render(request, 'web_yoga/product.html')

def pricing(request):
    return render(request, 'web_yoga/pricing.html')

def yoga_online(request):
    return render(request, 'web_yoga/yoga_online.html')

def contact(request):
    return render(request, 'web_yoga/contact.html')