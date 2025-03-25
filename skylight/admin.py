from django.contrib import admin
from skylight.models import Contact,Item,Cart,Booking

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "date")  

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image_url")

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user",)  
    filter_horizontal = ("items",)  

admin.site.register(Booking)
