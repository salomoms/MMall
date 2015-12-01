from django.forms import modelformset_factory
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from ecommerce.forms import CustomerForm, CartForm
from ecommerce.models import Category, Product, Customer, Cart


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
        customer_form = modelformset_factory(Customer, form=CustomerForm)

        if request.method == 'POST':

            customer_form = customer_form(request.POST)
            if customer_form.is_valid():
                customer = customer_form.save()

                request.session['customer'] = {'id': customer[0].id, 'name': customer[0].name, 'email': customer[0].name, 'address': customer[0].address}
                return redirect('/delivery')

    else:
        return redirect('/delivery')

    return render_to_response('ecommerce/customer_form.html', {'form': customer_form}, RequestContext(request))


def delivery(request):
    print request.session.get('customer')
    cart_form = modelformset_factory(Cart, form=CartForm)
    if request.method == 'POST':
        pass
    else:
        pass

    return render(request, 'ecommerce/cart_item.html', {'form': cart_form})