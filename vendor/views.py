from django.http import JsonResponse
from rest_framework.decorators import api_view
from vendor.models import Vendor
from .serializers import VendorsSerializer

# Create a new vendor.
@api_view(['POST'])
def vendor_registration(request):
    if request.method == 'POST':
        serializer = VendorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 'Vendor registration completed'})
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'Invalid request method'})

# Get all vendors details.
@api_view(['GET'])
def vendorsList(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serialized_date = VendorsSerializer(vendors, many=True)
        return JsonResponse({'vendors':serialized_date.data})
    return JsonResponse({'error':'invalid request'})

# Retrieve a specific vendor's details.
@api_view(['GET']) 
def vendorDetails(request):
    if request.method == 'GET':
        vendor_id = request.GET.get('vendor_id')
        if vendor_id is None:
            return JsonResponse({'error': 'Vendor ID is required'})
        
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            serialized_data = VendorsSerializer(vendor)
            return JsonResponse({'vendor': serialized_data.data})
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor does not exist'})
    return JsonResponse({'error': 'invalid request'})
    

# Update a vendor's details.
@api_view(['PUT'])
def update_vendor_details(request):
    vendor_id = request.data.get('vendor_id')
    if not vendor_id:
        return JsonResponse({'error': 'vendor_id is required in the request body'})

    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return JsonResponse({'error': 'Vendor not found'})
    
    if request.method == 'PUT':
        serialized_data = VendorsSerializer(vendor, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data)
        return JsonResponse(serialized_data.errors)
    return JsonResponse({'error': 'Invalid request method'})

# Delete a vendor.
@api_view(['DELETE'])
def delete_vendor_details(request):
    vendor_id = request.data.get('vendor_id')
    if not vendor_id:
        return JsonResponse({'error': 'vendor_id is required in the request body'})

    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return JsonResponse({'error': 'Vendor not found'})
    
    if request.method == 'DELETE':
        vendor.delete()
        return JsonResponse({'message': 'Vendor details deleted successfully'})
    return JsonResponse({'error': 'Invalid request method'})