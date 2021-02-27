from django.shortcuts import render

iphone_price = 60000

def new_launches(request):
    return render(request, 'iphone/new launches.html', context={'iphone': iphone_price})


def new_phones(request):
    return render(request, 'iphone/new phones.html', context={'iphone': iphone_price})


def popular_products(request):
    return render(request, 'iphone/popular products.html', context={'iphone': iphone_price})


def best_selling(request):
    return render(request, 'iphone/best selling.html', context={'iphone': iphone_price})




