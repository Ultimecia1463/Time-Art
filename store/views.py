from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order, OrderItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'store/register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'store/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.stock <= 0:
        return redirect('home')

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if cart_item.quantity < product.stock:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)

    total = 0
    for item in items:
        item.subtotal = item.quantity * item.product.price
        total += item.subtotal

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total
    })


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart')

    total = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product_name=item.product.name,
            price=item.product.price,
            quantity=item.quantity
        )

        item.product.stock -= item.quantity
        item.product.save()
        item.delete()

    return render(request, 'store/success.html', {
        'order': order
    })



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    return render(request, 'store/product_detail.html', {
        'product': product
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/orders.html', {'orders': orders})
