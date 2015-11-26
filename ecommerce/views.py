from django.shortcuts import render, redirect
from ecommerce.models import Category, Product


def index(request):
    category = Category.objects.all()[:4]
    context = {
        'categories': category,
        'request': request
    }

    return render(request, 'ecommerce/index.html', context)


def addToCart(request, id, slug):
    cart = request.session.get('cart', {})
    total_price = request.session.get('total_price', 0)
    if slug in cart:
        cart[slug]['total'] += 1
        cart[slug]['total_price'] = cart[slug]['total'] * cart[slug]['price']
        total_price += cart[slug]['price']
    else:
        product = Product.objects.get(pk=id)
        cart.update({
                    slug: {
                        'product': {
                            'name': product.title,
                            'price': int(product.price),
                            'brand': product.brand_id,
                            'category': product.category_id,
                            'total_price': int(product.price),
                        },
                        'total': 1}})
        total_price += int(product.price)

    request.session['cart'] = cart
    request.session['total_price'] = total_price

    return redirect('/')


def cart(request):
    context = {}
    return render(request, 'ecommerce/cart.html', context)


def checkout(request):
    if request.session.get('customer', None) is None:
        pass
    else:
        pass

    pass
