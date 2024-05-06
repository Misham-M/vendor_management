from django.urls import path
from vendor import views

urlpatterns = [
    path('vendor-registration', views.vendor_registration, name='vendor_registration'),
    path('vendors', views.vendorsList, name='vendorsList'),
    path('vendor-details', views.vendorDetails, name='vendorDetails'),
    path('update_vendor_details', views.update_vendor_details, name='update_vendor_details'),
    path('delete-vendor', views.delete_vendor_details, name='delete_vendor_details'),
]
 