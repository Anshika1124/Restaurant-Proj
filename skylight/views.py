from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from datetime import datetime
from skylight.models import Contact,Item, Cart,CartItem,Booking
from django.contrib import messages
from .forms import ItemForm


# Create your views here.
def index(request):
	context={
		"variable":"Anshika"
	}
	messages.success(request,"This is a text message")
	return render(request,'index.html',context)
	#return HttpResponse("this is a homepage")

def about(request):
		return render(request,'about.html')

	#return HttpResponse("this is a aboutpage")


def contact(request):
   if request.method == 'POST':
       name = request.POST.get('name',' ')
       email = request.POST.get('email',' ')
       subject = request.POST.get('subject',' ')
       message = request.POST.get('message',' ')

       contact = Contact(name=name, email=email, subject=subject, message=message, 
		  date=datetime.today())
       contact.save()
   return render(request, 'contact.html') 


def book_table(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        datetime = request.POST.get("datetime")
        people = request.POST.get("people")
        message = request.POST.get("message")

        Booking.objects.create(name=name, email=email, datetime=datetime, people=people, message=message)
        messages.success(request, "Your table has been booked successfully!")

        return redirect("book_table")  

    return render(request, "booktable.html")


ITEMS = {
    1: {"name": "Burger", "price": 120, "image": "https://static.vecteezy.com/system/resources/thumbnails/023/809/530/small/a-flying-burger-with-all-the-layers-ai-generative-free-photo.jpg"},
    2: {"name": "Pizza", "price": 250, "image": "https://t3.ftcdn.net/jpg/00/27/57/96/360_F_27579652_tM7V4fZBBw8RLmZo0Bi8WhtO2EosTRFD.jpg"},
    3: {"name": "Pasta", "price": 220, "image": "https://media.istockphoto.com/id/1325172440/photo/spaghetti-alla-puttanesca-italian-pasta-dish-with-tomatoes-black-olives-capers-anchovies-and.jpg?s=612x612&w=0&k=20&c=ieMxGg7flhSltOMDpuLZINAWYT2W2WDjJTlwoUWuwH4="},
    4: {"name": "Momo", "price": 150, "image": "https://c.ndtvimg.com/2020-01/2brioi88_momos_625x300_21_January_20.jpg"},
    5: {"name": "Shahi Paneer", "price": 550, "image": "https://media.istockphoto.com/id/1305516603/photo/shahi-paneer-or-paneer-kadai.jpg?s=612x612&w=0&k=20&c=V5xD4I1ciIjtyoH0FzuNeFnAl7oV9RJAoNs52X6pgE4="},
}

def menu(request):
    items = Item.objects.all()  
    print("items")
    return render(request, "menu.html", {"items": items})



def cart(request):
    cart = Cart.objects.filter(user=request.user).first()  

    if not cart:
        return render(request, 'cart.html', {'cart_items': [], 'total_price': 0})

    cart_items = CartItem.objects.filter(cart=cart)  
    total_price = sum(item.item.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = CartItem.objects.filter(cart=cart, item_id=item_id).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1 
            cart_item.save()
        else:
            cart_item.delete() 
        messages.success(request, "Item updated in cart!")
    else:
        messages.error(request, "Item not found in cart.")

    return redirect('cart')


def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = sum(item.item.price * item.quantity for item in cart_items)

    if request.method == "POST":
        cart_items.delete()
        return redirect('cart') 

    return render(request, 'checkout.html', {'total_price': total_price})


def add_to_cart(request, item_id):

    item = get_object_or_404(Item, id=item_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)

    if not created:
        cart_item.quantity += 1  
    cart_item.save()

    messages.success(request, f"{item.name} added to cart! (Quantity: {cart_item.quantity})")
    return redirect('cart')

def chef_Detail(request):
		return render(request,'chef_Detail.html')
