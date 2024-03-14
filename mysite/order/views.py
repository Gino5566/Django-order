from django.shortcuts import get_object_or_404,render,redirect
from django.db.models import Sum
from django.http import HttpResponse
from django.contrib import messages
from .models import Food,Shoppingcart,Option,Drink,Order,Order_Item


# Create your views here.


def index(request):
    latest_food_list = Food.objects.order_by('id')
    latest_drink_list = Drink.objects.order_by('id')
    total = Shoppingcart.objects.aggregate(total=Sum('subtotal'))['total']
    if total == None:total=0
    context = {
        'food': latest_food_list,
        'drink':latest_drink_list,
        'total':total
    }
    return render(request,"menu.html",context)

def foodetail(request, food_id):
    coin=0
    remark=""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        selected_options = request.POST.getlist('options')


        food = Food.objects.get(pk=food_id)

        for option_id in selected_options:
            option = Option.objects.get(pk=option_id)
            coin+=option.price
            remark+=option.name+"，"


        subtotal = (food.price+coin) * quantity


        shopping_cart = Shoppingcart(name=food.name, remark=remark[:-1], count=quantity, subtotal=subtotal)
        shopping_cart.save()


        return redirect('../../')
    
    food = get_object_or_404(Food, pk=food_id)
    return render(request, "foodetail.html", {'food': food})

def drinkdetail(request,drink_id):
    coin=0
    remark=""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        temperature = request.POST.get('temperature')
        size = request.POST.get('size')
        if(temperature=="hot"):
            remark+="熱的，"
        else:
            remark+="冰的，"

        if(size=="short"):
            remark+="小杯"
        else:
            remark+="大杯"
            coin+=5

        drink = Drink.objects.get(pk=drink_id)

        subtotal = (drink.price+coin) * quantity

        shopping_cart = Shoppingcart(name=drink.name, remark=remark, count=quantity, subtotal=subtotal)
        shopping_cart.save()

        return redirect('../../')


    drink = get_object_or_404(Drink, pk=drink_id)
    return render(request, "drinkdetail.html", {'drink': drink})

def shoppingcart(request):
    latest_shopcart_list=Shoppingcart.objects.order_by('id')
    total = Shoppingcart.objects.aggregate(total=Sum('subtotal'))['total']
    context={
        'shopcart':latest_shopcart_list,
        'total':total
    }
    return render(request,"shoppingcart.html",context)

def delete_order(request, shop_id):
    order_item = Shoppingcart.objects.get(pk=shop_id)
    order_item.delete()
    return redirect('../../shoppingcart')


def complete_order(request):
    number="ORD#1"
    if Order.objects.exists()!=False:
        latest_order = Order.objects.latest('order_number')
        latest_number=latest_order.order_number
        number="ORD#"+str(int(latest_number[4:])+1)

    total = Shoppingcart.objects.aggregate(total=Sum('subtotal'))['total']    

    shopping_cart_items = Shoppingcart.objects.all()

    order_items = []

    for item in shopping_cart_items:
        order_item = Order_Item(
            order_number=number,
            name=item.name,
            remark=item.remark,
            count=item.count,
            subtotal=item.subtotal
        )
        order_item.save()
        order_items.append(order_item)

    order = Order(order_number=number,
                    total=total
                    )

    order.save()

    order.order_items.set(order_items)

    order.save()


    Shoppingcart.objects.all().delete()


    return redirect('../')

def orderlist(request):
    orderlist=Order.objects.order_by('id')
    context={
        'orderlist':orderlist,
    }
    return render(request,"orderlist.html",context)

def orderdetail(request,order_id):
    orderdetail=get_object_or_404(Order,pk=order_id)
    return render(request,"orderdetail.html",{'orderdetail':orderdetail})
