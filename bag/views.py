from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bundle = None
    if 'product_bundle' in request.POST:
        bundle = request.POST['product_bundle']
    bag = request.session.get('bag', {})

    print("POST REQUEST: ", request.POST)

    if bundle:
        if item_id in list(bag.keys()):
            if bundle in bag[item_id]['items_by_bundle'].keys():
                bag[item_id]['items_by_bundle'][bundle] += quantity
            else:
                bag[item_id]['items_by_bundle'][bundle] = quantity
        else:
            bag[item_id] = {'items_by_bundle': {bundle: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    print(f"Bag updated: {bag}")
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))

    bundle = None
    if 'product_bundle' in request.POST:
        bundle = request.POST['product_bundle']
    bag = request.session.get('bag', {})

    if bundle:
        if quantity > 0:
            bag[item_id]['items_by_bundle'][bundle] = quantity
        else:
            del bag[item_id]['items_by_bundle'][bundle]
            if not bag[item_id]['items_by_bundle']:
            bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    print(f"Bag updated: {bag}")
    return redirect(reverse('view_bag'))
    
def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try: 
    bundle = None
        if 'product_bundle' in request.POST:
            bundle = request.POST['product_bundle']
        bag = request.session.get('bag', {})

        if bundle:
            del bag[item_id]['items_by_bundle'][bundle]
            if not bag[item_id]['items_by_bundle']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        print(f"Bag updated: {bag}")
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
        