from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages 

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bundle = None
    if 'product_bundle' in request.POST:
        bundle = request.POST['product_bundle']
    bag = request.session.get('bag', {})

    if bundle:
        if item_id in list(bag.keys()):
            if bundle in bag[item_id]['items_by_bundle'].keys():
                bag[item_id]['items_by_bundle'][bundle] += quantity
                messages.success(request, f'Updated bundle {bundle.upper()} {product.name} to {bag[item_id]["items_by_bundle"][bundle]}')
            else:
                bag[item_id]['items_by_bundle'][bundle] = quantity
                messages.success(request, f'Added bundle {bundle.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_bundle': {bundle: quantity}}
            messages.success(request, f'Added bundle {bundle.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(f"Bag updated: {bag}")
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bundle = None
    if 'product_bundle' in request.POST:
        bundle = request.POST['product_bundle']
    bag = request.session.get('bag', {})

    if bundle:
        if quantity > 0:
            bag[item_id]['items_by_bundle'][bundle] = quantity
            messages.success(request, f'Updated bundle {bundle.upper()} {product.name} to {bad[item_id]["items_by_bundle"][bundle]}')
        else:
            del bag[item_id]['items_by_bundle'][bundle]
            if not bag[item_id]['items_by_bundle']:
                bag.pop(item_id)
            messages.success(request, f'Removed bundle {bundle.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
    
def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id) 
        bundle = None
        if 'product_bundle' in request.POST:
            bundle = request.POST['product_bundle']
        bag = request.session.get('bag', {})

        if bundle:
            del bag[item_id]['items_by_bundle'][bundle]
            if not bag[item_id]['items_by_bundle']:
                bag.pop(item_id)
            messages.success(request, f'Removed bundle {bundle.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: (e)')
        return HttpResponse(status=500)
            