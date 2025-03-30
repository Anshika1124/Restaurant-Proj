from django.contrib import admin
from django.urls import path
from skylight import views

urlpatterns = [
	path("",views.index,name='home'),
	path("about/",views.about,name='about'),
	path("Menu/",views.menu,name='menu'),
	path("contact/",views.contact,name='contact'),
	path("book-table/",views.book_table,name='book_table'),
	path("cart/",views.cart,name='cart'),
    path('add_to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('chef_Detail/', views.chef_Detail, name='chef_Detail'),

]
