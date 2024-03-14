from django.contrib import admin
from .models import Food,Option,Shoppingcart,Drink,Order,Order_Item
# Register your models here.


admin.site.register(Food)
admin.site.register(Option)
admin.site.register(Shoppingcart)
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(Order_Item)