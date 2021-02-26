from django.shortcuts import render


def new_launches(request):
    return render(request, 'iphone/new launches.html', context={'iphone': 60000})


def new_phones(request):
    return render(request, 'iphone/new phones.html', context={'iphone': 50000})


def popular_products(request):
    return render(request, 'iphone/popular products.html', context={'iphone': 40000})


def best_selling(request):
    return render(request, 'iphone/best selling.html', context={'iphone': 30000})




