from django.urls import path
from purchase import views


urlpatterns = [
    path('create_purchase_order', views.create_purchase_order, name='create_purchase_order'),
    path('list_purchase_orders', views.list_purchase_orders, name='list_purchase_orders'),
    path('retrieve_purchase_order', views.retrieve_purchase_order, name='retrieve_purchase_order'),
    path('update_purchase_order', views.update_purchase_order, name='update_purchase_order'),
    path('delete_purchase_order', views.delete_purchase_order, name='delete_purchase_order')
]
