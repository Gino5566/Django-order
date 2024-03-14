from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('food/<int:food_id>/', views.foodetail,name='foodetail'),
path('drink/<int:drink_id>/', views.drinkdetail,name='drinkdetail'),
path('shoppingcart/',views.shoppingcart,name='shoppingcart'),
path('delete/<int:shop_id>/',views.delete_order,name='delete_order'),
path('complete-order/',views.complete_order,name='complete_order'),
path('orderlist/',views.orderlist,name='orderlist'),
path('orderdetail/<int:order_id>/',views.orderdetail,name='orderdetail')
]
