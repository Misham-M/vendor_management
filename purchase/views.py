from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

# Create a purchase order
@api_view(['POST'])
def create_purchase_order(request):
    if request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'})

# List all purchase orders with an option to filter by vendor
@api_view(['GET'])
def list_purchase_orders(request):
    if request.method == 'GET':
        vendor_id = request.GET.get('vendor_id')
        if vendor_id:
            purchase_orders = PurchaseOrder.objects.filter(vendor=vendor_id)
        else:
            purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return JsonResponse({'data': serializer.data}, safe=False)
    return JsonResponse({'error': 'Invalid request method'})

# Retrieve details of a specific purchase order
@api_view(['GET'])
def retrieve_purchase_order(request):   
    if request.method == 'GET':
        purchase_order = request.GET.get('purchase_order_id')
        order = PurchaseOrder.objects.get(po_number=purchase_order)
        serializer = PurchaseOrderSerializer(order)
        return JsonResponse({'data': serializer.data})

# Update a purchase order
@api_view(['PUT'])
def update_purchase_order(request):
    po_id = request.data.get('po_id')
    purchase_order = PurchaseOrder.objects.get(po_number=po_id)
    if request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchase_order, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data})
        return JsonResponse({'errors': serializer.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'})
    

# Delete a purchase order
@api_view(['DELETE'])
def delete_purchase_order(request):
    po_id = request.data.get('po_id')
    purchase_order = PurchaseOrder.objects.get(po_number=po_id)
    if request.method == 'DELETE':
        purchase_order.delete()
        return JsonResponse({'message': 'Purchase order deleted successfully'}, status=204)
    return JsonResponse({'error': 'Invalid request method'})
    
