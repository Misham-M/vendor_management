from rest_framework import serializers
from vendor.models import Vendor

class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'