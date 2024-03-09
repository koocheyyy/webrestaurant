# import json


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.shortcuts import render

# from rest_framework import generics
# from . import models, serializers, permissions

# # Create your views here.
# class PlaceList(generics.ListCreateAPIView):
#   serializer_class = serializers.PlaceSerializer

#   def get_queryset(self):
#     return models.Place.objects.filter(owner_id=self.request.user.id)

#   def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)

# class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
#   permission_classes = [permissions.IsOwnerOrReadOnly]
#   serializer_class = serializers.PlaceDetailSerializer
#   queryset = models.Place.objects.all()

# class CategoryList(generics.CreateAPIView):
#   permission_classes = [permissions.PlaceOwnerOrReadOnly]
#   serializer_class = serializers.CategorySerializer

# class CategoryDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#   permission_classes = [permissions.PlaceOwnerOrReadOnly]
#   serializer_class = serializers.CategorySerializer
#   queryset = models.Category.objects.all()

# class MenuItemList(generics.CreateAPIView):
#   permission_classes = [permissions.PlaceOwnerOrReadOnly]
#   serializer_class = serializers.MenuItemSerializer

# class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#   permission_classes = [permissions.PlaceOwnerOrReadOnly]
#   serializer_class = serializers.MenuItemSerializer
#   queryset = models.MenuItem.objects.all()

# def home(request):
#   return render(request, 'index.html')



# @csrf_exempt
# def create_payment_intent(request):
 
#     data = json.loads(request.body)
      
#     order = models.Order.objects.create(
#     place_id = data['place'],
#     table = data['table'],
#     detail = json.dumps(data['detail']),
#     amount = data['amount'],
      
#     )

#     return JsonResponse({
#       "success": True,
#       "order": order.id,
#     })


# class OrderList(generics.ListAPIView):
#   serializer_class = serializers.OrderSerializer

#   def get_queryset(self):
#     return models.Order.objects.filter(place__owner_id=self.request.user.id, place_id=self.request.GET.get('place'))

# class OrderDetail(generics.UpdateAPIView):
#   permission_classes = [permissions.PlaceOwnerOrReadOnly]
#   serializer_class = serializers.OrderSerializer
#   queryset = models.Order.objects.all()

# import json
# from rest_framework.views import APIView
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# from rest_framework import generics
# from . import models, serializers
# from .models import Tag  # Import the Tag model
# from .serializers import TagSerializer  # Import the Tag serializer
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
# from rest_framework import status
# from .models import UserSession
# from .serializers import UserSessionSerializer
# from django.utils.crypto import get_random_string
# from .serializers import InvoiceSerializer


# # Create your views here.
# class PlaceList(generics.ListCreateAPIView):
#     serializer_class = serializers.PlaceSerializer

#     def get_queryset(self):
#         return models.Place.objects.filter(owner_id=self.request.user.id)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = serializers.PlaceDetailSerializer
#     queryset = models.Place.objects.all()

# class CategoryList(generics.CreateAPIView):
#     serializer_class = serializers.CategorySerializer

# class CategoryDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.CategorySerializer
#     queryset = models.Category.objects.all()

# class MenuItemList(generics.CreateAPIView):
#     serializer_class = serializers.MenuItemSerializer

# class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.MenuItemSerializer
#     queryset = models.MenuItem.objects.all()

# def home(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def create_payment_intent(request):
#     data = json.loads(request.body)
#     # Extract session ID from the request data
#     session_id = data.get('sessionId')

#     order = models.Order.objects.create(
#         place_id=data['place'],
#         table=data['table'],
#         detail=json.dumps(data['detail']),
#         amount=data['amount'],
#         session_id=session_id,  # Save session ID with the order
#         email=data['email'],    # Save email with the order
#     )
#     return JsonResponse({
#         "success": True,
#         "order": order.id,
#     })

    
# @csrf_exempt
# def confirmPayment(request):
#     try:
#         data = json.loads(request.body)
#         session_id = data.get('sessionId')

#         # Find the corresponding UserSession and set it to inactive
#         user_session = UserSession.objects.get(session_id=session_id)
#         user_session.is_active = False
#         user_session.save()

#         return JsonResponse({"success": True, "message": "Payment confirmed and session updated."})

#     except UserSession.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Session not found."})
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)})


# class OrderList(generics.ListAPIView):
#     serializer_class = serializers.OrderSerializer

#     def get_queryset(self):
#         return models.Order.objects.filter(place__owner_id=self.request.user.id, place_id=self.request.GET.get('place'))

# class OrderDetail(generics.UpdateAPIView):
#     serializer_class = serializers.OrderSerializer
#     queryset = models.Order.objects.all()

# class TagList(APIView):
#     def get(self, request, format=None):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
    
# class TagCreate(CreateAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.TagSerializer
    
    
# class TagDelete(APIView):
#     """
#     Delete a specific tag.
#     """
#     def delete(self, request, pk, format=None):
#         try:
#             tag = Tag.objects.get(pk=pk)
#             tag.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Tag.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        

# class CreateSessionView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         table = request.data.get('table')  # Get the table number from the request

#         if not email:
#             return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Logic to create a session and sessionId including the table number
#         session = UserSession.create_session_for_email(email, table)
#         serializer = UserSessionSerializer(session)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CheckSessionView(APIView):
#     def post(self, request):
#         table = request.data.get('table')  # Get the table number from the request

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Check for any active sessions for the given table
#         active_sessions = UserSession.objects.filter(table=table, is_active=True)

#         if active_sessions.exists():
#             sessions_data = [{"session_id": session.session_id, "email": session.email} for session in active_sessions]
#             return Response({
#                 "active_sessions": True,
#                 "sessions": sessions_data,
#                 "message": "Active sessions found for this table."
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"active_sessions": False}, status=status.HTTP_200_OK)


# class GenerateInvoiceIDView(APIView):
#     def get(self, request, format=None):
#         # Generate a unique invoice ID
#         invoice_id = get_random_string(length=12)  # Adjust the length as needed
#         return Response({'invoice_id': invoice_id})
    
# class CreateInvoiceView(APIView):
#     def post(self, request, format=None):
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# import json
# from rest_framework.views import APIView
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# from rest_framework import generics
# from . import models, serializers
# from .models import Tag  # Import the Tag model
# from .serializers import TagSerializer  # Import the Tag serializer
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
# from rest_framework import status
# from .models import UserSession
# from .serializers import UserSessionSerializer
# from django.utils.crypto import get_random_string
# from .serializers import InvoiceSerializer


# # Create your views here.
# class PlaceList(generics.ListCreateAPIView):
#     serializer_class = serializers.PlaceSerializer

#     def get_queryset(self):
#         return models.Place.objects.filter(owner_id=self.request.user.id)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = serializers.PlaceDetailSerializer
#     queryset = models.Place.objects.all()

# class CategoryList(generics.CreateAPIView):
#     serializer_class = serializers.CategorySerializer

# class CategoryDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.CategorySerializer
#     queryset = models.Category.objects.all()

# class MenuItemList(generics.CreateAPIView):
#     serializer_class = serializers.MenuItemSerializer

# class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.MenuItemSerializer
#     queryset = models.MenuItem.objects.all()

# def home(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def create_payment_intent(request):
#     data = json.loads(request.body)
#     # Extract session ID from the request data
#     session_id = data.get('sessionId')

#     order = models.Order.objects.create(
#         place_id=data['place'],
#         table=data['table'],
#         detail=json.dumps(data['detail']),
#         amount=data['amount'],
#         session_id=session_id,  # Save session ID with the order
#         email=data['email'],    # Save email with the order
#     )
#     return JsonResponse({
#         "success": True,
#         "order": order.id,
#     })

    
# @csrf_exempt
# def confirmPayment(request):
#     try:
#         data = json.loads(request.body)
#         session_id = data.get('sessionId')

#         # Find the corresponding UserSession and set it to inactive
#         user_session = UserSession.objects.get(session_id=session_id)
#         user_session.is_active = False
#         user_session.save()

#         return JsonResponse({"success": True, "message": "Payment confirmed and session updated."})

#     except UserSession.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Session not found."})
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)})


# class OrderList(generics.ListAPIView):
#     serializer_class = serializers.OrderSerializer

#     def get_queryset(self):
#         return models.Order.objects.filter(place__owner_id=self.request.user.id, place_id=self.request.GET.get('place'))

# class OrderDetail(generics.UpdateAPIView):
#     serializer_class = serializers.OrderSerializer
#     queryset = models.Order.objects.all()

# class TagList(APIView):
#     def get(self, request, format=None):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
    
# class TagCreate(CreateAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.TagSerializer
    
    
# class TagDelete(APIView):
#     """
#     Delete a specific tag.
#     """
#     def delete(self, request, pk, format=None):
#         try:
#             tag = Tag.objects.get(pk=pk)
#             tag.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Tag.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        

# class CreateSessionView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         table = request.data.get('table')  # Get the table number from the request

#         if not email:
#             return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Logic to create a session and sessionId including the table number
#         session = UserSession.create_session_for_email(email, table)
#         serializer = UserSessionSerializer(session)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CheckSessionView(APIView):
#     def post(self, request):
#         table = request.data.get('table')  # Get the table number from the request

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Check for any active sessions for the given table
#         active_sessions = UserSession.objects.filter(table=table, is_active=True)

#         if active_sessions.exists():
#             sessions_data = [{"session_id": session.session_id, "email": session.email} for session in active_sessions]
#             return Response({
#                 "active_sessions": True,
#                 "sessions": sessions_data,
#                 "message": "Active sessions found for this table."
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"active_sessions": False}, status=status.HTTP_200_OK)


# class GenerateInvoiceIDView(APIView):
#     def get(self, request, format=None):
#         # Generate a unique invoice ID
#         invoice_id = get_random_string(length=12)  # Adjust the length as needed
#         return Response({'invoice_id': invoice_id})
    
# class CreateInvoiceView(APIView):
#     def post(self, request, format=None):
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class InvoiceListView(generics.ListAPIView):
#     serializer_class = serializers.InvoiceSerializer

#     def get_queryset(self):
#         return models.Invoice.objects.all()


# import json
# from rest_framework.views import APIView
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# from rest_framework import generics
# from . import models, serializers
# from .models import Tag  # Import the Tag model
# from .serializers import TagSerializer  # Import the Tag serializer
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
# from rest_framework import status
# from .models import UserSession
# from .serializers import UserSessionSerializer
# from django.utils.crypto import get_random_string
# from .serializers import InvoiceSerializer
# from rest_framework.decorators import api_view
# from .models import Invoice


# # Create your views here.
# class PlaceList(generics.ListCreateAPIView):
#     serializer_class = serializers.PlaceSerializer

#     def get_queryset(self):
#         return models.Place.objects.filter(owner_id=self.request.user.id)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = serializers.PlaceDetailSerializer
#     queryset = models.Place.objects.all()

# class CategoryList(generics.CreateAPIView):
#     serializer_class = serializers.CategorySerializer

# class CategoryDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.CategorySerializer
#     queryset = models.Category.objects.all()

# class MenuItemList(generics.CreateAPIView):
#     serializer_class = serializers.MenuItemSerializer

# class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.MenuItemSerializer
#     queryset = models.MenuItem.objects.all()

# def home(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def create_payment_intent(request):
#     data = json.loads(request.body)
#     # Extract session ID from the request data
#     session_id = data.get('sessionId')

#     order = models.Order.objects.create(
#         place_id=data['place'],
#         table=data['table'],
#         detail=json.dumps(data['detail']),
#         amount=data['amount'],
#         session_id=session_id,  # Save session ID with the order
#         email=data['email'],    # Save email with the order
#     )
#     return JsonResponse({
#         "success": True,
#         "order": order.id,
#     })

    
# @csrf_exempt
# def confirmPayment(request):
#     try:
#         data = json.loads(request.body)
#         session_id = data.get('sessionId')

#         # Find the corresponding UserSession and set it to inactive
#         user_session = UserSession.objects.get(session_id=session_id)
#         user_session.is_active = False
#         user_session.save()

#         return JsonResponse({"success": True, "message": "Payment confirmed and session updated."})

#     except UserSession.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Session not found."})
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)})


# class OrderList(generics.ListAPIView):
#     serializer_class = serializers.OrderSerializer

#     def get_queryset(self):
#         return models.Order.objects.filter(place__owner_id=self.request.user.id, place_id=self.request.GET.get('place'))

# class OrderDetail(generics.UpdateAPIView):
#     serializer_class = serializers.OrderSerializer
#     queryset = models.Order.objects.all()

# class TagList(APIView):
#     def get(self, request, format=None):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
    
# class TagCreate(CreateAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.TagSerializer
    
    
# class TagDelete(APIView):
#     """
#     Delete a specific tag.
#     """
#     def delete(self, request, pk, format=None):
#         try:
#             tag = Tag.objects.get(pk=pk)
#             tag.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Tag.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        

# class CreateSessionView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         table = request.data.get('table')  # Get the table number from the request

#         if not email:
#             return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Logic to create a session and sessionId including the table number
#         session = UserSession.create_session_for_email(email, table)
#         serializer = UserSessionSerializer(session)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CheckSessionView(APIView):
#     def post(self, request):
#         table = request.data.get('table')  # Get the table number from the request

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Check for any active sessions for the given table
#         active_sessions = UserSession.objects.filter(table=table, is_active=True)

#         if active_sessions.exists():
#             sessions_data = [{"session_id": session.session_id, "email": session.email} for session in active_sessions]
#             return Response({
#                 "active_sessions": True,
#                 "sessions": sessions_data,
#                 "message": "Active sessions found for this table."
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"active_sessions": False}, status=status.HTTP_200_OK)


# class GenerateInvoiceIDView(APIView):
#     def get(self, request, format=None):
#         # Generate a unique invoice ID
#         invoice_id = get_random_string(length=12)  # Adjust the length as needed
#         return Response({'invoice_id': invoice_id})
    
# class CreateInvoiceView(APIView):
#     def post(self, request, format=None):
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class InvoiceListView(generics.ListAPIView):
#     serializer_class = serializers.InvoiceSerializer

#     def get_queryset(self):
#         return models.Invoice.objects.all()




# @api_view(['PUT'])
# def update_invoice_status(request, invoice_id):
#     try:
#         invoice = Invoice.objects.get(invoice_number=invoice_id)  # Use invoice_number to get the Invoice
#         invoice_data = request.data

#         invoice.paid = invoice_data.get('paid', invoice.paid)
#         invoice.save()

#         return Response({'success': True, 'message': 'Invoice status updated.'})

#     except Invoice.DoesNotExist:
#         return Response({'success': False, 'error': 'Invoice not found.'}, status=404)

#     except Exception as e:
#         return Response({'success': False, 'error': str(e)}, status=500)


# import json
# from rest_framework.views import APIView
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# from rest_framework import generics
# from . import models, serializers
# from .models import Tag  # Import the Tag model
# from .serializers import TagSerializer  # Import the Tag serializer
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
# from rest_framework import status
# from .models import UserSession
# from .serializers import UserSessionSerializer
# from django.utils.crypto import get_random_string
# from .serializers import InvoiceSerializer
# from rest_framework.decorators import api_view
# from .models import Invoice
# from django.utils import timezone
# import datetime
# from .models import MenuItem
# from django.db.models import F, Sum, Count, IntegerField
# from django.db.models.functions import Cast
# from django.contrib.postgres.aggregates import ArrayAgg
# from django.db.models.fields.json import KeyTextTransform
# from django.db.models import OuterRef, Subquery, IntegerField
# from django.db.models.functions import Coalesce
# from collections import defaultdict
# from operator import itemgetter
# from collections import Counter
# from django.utils import timezone
# from datetime import timedelta, datetime
# from django.db.models.functions import ExtractWeekDay, ExtractHour
# from django.db.models.functions import ExtractHour
# from django.db.models import Count, Avg




# # Create your views here.
# class PlaceList(generics.ListCreateAPIView):
#     serializer_class = serializers.PlaceSerializer

#     def get_queryset(self):
#         return models.Place.objects.filter(owner_id=self.request.user.id)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = serializers.PlaceDetailSerializer
#     queryset = models.Place.objects.all()

# class CategoryList(generics.CreateAPIView):
#     serializer_class = serializers.CategorySerializer

# class CategoryDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.CategorySerializer
#     queryset = models.Category.objects.all()

# class MenuItemList(generics.CreateAPIView):
#     serializer_class = serializers.MenuItemSerializer

# class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
#     serializer_class = serializers.MenuItemSerializer
#     queryset = models.MenuItem.objects.all()

# def home(request):
#     return render(request, 'index.html')

# @csrf_exempt
# def create_payment_intent(request):
#     data = json.loads(request.body)
#     # Extract session ID from the request data
#     session_id = data.get('sessionId')

#     order = models.Order.objects.create(
#         place_id=data['place'],
#         table=data['table'],
#         detail=json.dumps(data['detail']),
#         amount=data['amount'],
#         session_id=session_id,  # Save session ID with the order
#         email=data['email'],    # Save email with the order
#     )
#     return JsonResponse({
#         "success": True,
#         "order": order.id,
#     })

    
# @csrf_exempt
# def confirmPayment(request):
#     try:
#         data = json.loads(request.body)
#         session_id = data.get('sessionId')

#         # Find the corresponding UserSession and set it to inactive
#         user_session = UserSession.objects.get(session_id=session_id)
#         user_session.is_active = False
#         user_session.save()

#         return JsonResponse({"success": True, "message": "Payment confirmed and session updated."})

#     except UserSession.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Session not found."})
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)})


# class OrderList(generics.ListAPIView):
#     serializer_class = serializers.OrderSerializer

#     def get_queryset(self):
#         return models.Order.objects.filter(place__owner_id=self.request.user.id, place_id=self.request.GET.get('place'))

# class OrderDetail(generics.UpdateAPIView):
#     serializer_class = serializers.OrderSerializer
#     queryset = models.Order.objects.all()

# class TagList(APIView):
#     def get(self, request, format=None):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
    
# class TagCreate(CreateAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.TagSerializer
    
    
# class TagDelete(APIView):
#     """
#     Delete a specific tag.
#     """
#     def delete(self, request, pk, format=None):
#         try:
#             tag = Tag.objects.get(pk=pk)
#             tag.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Tag.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        

# class CreateSessionView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         table = request.data.get('table')  # Get the table number from the request

#         if not email:
#             return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Logic to create a session and sessionId including the table number
#         session = UserSession.create_session_for_email(email, table)
#         serializer = UserSessionSerializer(session)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CheckSessionView(APIView):
#     def post(self, request):
#         table = request.data.get('table')  # Get the table number from the request

#         if not table:
#             return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Check for any active sessions for the given table
#         active_sessions = UserSession.objects.filter(table=table, is_active=True)

#         if active_sessions.exists():
#             sessions_data = [{"session_id": session.session_id, "email": session.email} for session in active_sessions]
#             return Response({
#                 "active_sessions": True,
#                 "sessions": sessions_data,
#                 "message": "Active sessions found for this table."
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"active_sessions": False}, status=status.HTTP_200_OK)


# class GenerateInvoiceIDView(APIView):
#     def get(self, request, format=None):
#         # Generate a unique invoice ID
#         invoice_id = get_random_string(length=12)  # Adjust the length as needed
#         return Response({'invoice_id': invoice_id})
    
# class CreateInvoiceView(APIView):
#     def post(self, request, format=None):
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class InvoiceListView(generics.ListAPIView):
#     serializer_class = serializers.InvoiceSerializer

#     def get_queryset(self):
#         return models.Invoice.objects.all()




# @api_view(['PUT'])
# def update_invoice_status(request, invoice_id):
#     try:
#         invoice = Invoice.objects.get(invoice_number=invoice_id)  # Use invoice_number to get the Invoice
#         invoice_data = request.data

#         invoice.paid = invoice_data.get('paid', invoice.paid)
#         invoice.save()

#         return Response({'success': True, 'message': 'Invoice status updated.'})

#     except Invoice.DoesNotExist:
#         return Response({'success': False, 'error': 'Invoice not found.'}, status=404)

#     except Exception as e:
#         return Response({'success': False, 'error': str(e)}, status=500)




# class PopularMenuItemThisWeek(APIView):
#     def get(self, request, format=None):
#         one_week_ago = timezone.now() - timedelta(days=7)
        
#         # Fetch all invoices from the last week that were paid
#         invoices = Invoice.objects.filter(issued_at__gte=one_week_ago, paid=True)
        
#         # Initialize a Counter to count the quantities of each MenuItem
#         item_counter = Counter()
        
#         # Iterate over invoices and update the counter for each item
#         for invoice in invoices:
#             for item in invoice.items:  # Assuming that items is a list of dicts with 'id' and 'quantity' keys
#                 item_id = item.get('id')
#                 quantity = item.get('quantity', 1)  # Default to 1 if quantity is not specified
#                 item_counter[item_id] += quantity
        
#         # Get the top 20 items by quantity ordered
#         top_items = item_counter.most_common(20)
        
#         # Extract the item IDs
#         top_item_ids = [item[0] for item in top_items]

#         # Retrieve the corresponding MenuItem objects for these IDs
#         menu_items = MenuItem.objects.filter(id__in=top_item_ids).in_bulk()

#         # Serialize the menu items
#         serialized_data = serializers.MenuItemSerializer(
#             [menu_items[item_id] for item_id in top_item_ids if item_id in menu_items],
#             many=True
#         ).data

#         # Add the quantity ordered to the serialized data
#         for item_data in serialized_data:
#             item_id = item_data['id']
#             item_data['ordered_quantity'] = item_counter[item_id]

#         return Response(serialized_data)

        
# class TotalSalesToday(APIView):
#     def get(self, request, format=None):
#         today = timezone.now().date()
#         total_sales = models.Invoice.objects.filter(
#             issued_at__date=today, 
#             paid=True
#         ).aggregate(Sum('total_amount'))

#         return Response({"total_sales": total_sales['total_amount__sum'] or 0})
    
    
# class TotalSalesThisWeek(APIView):
#     def get(self, request, format=None):
#         # Define the start of the week (e.g., Monday)
#         today = timezone.now().date()
#         start_of_week = today - timedelta(days=today.weekday())
#         end_of_week = start_of_week + timedelta(days=7)

#         # Filter the invoices within this week and sum the total_amount
#         total_sales_this_week = Invoice.objects.filter(
#             issued_at__date__range=(start_of_week, end_of_week),
#             paid=True
#         ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0  # Default to 0 if no sales

#         return Response({"total_sales_this_week": total_sales_this_week})

# class TotalSalesThisMonth(APIView):
#     def get(self, request, format=None):
#         today = timezone.now().date()
#         first_day_of_month = today.replace(day=1)
#         last_day_of_month = today.replace(day=28) + timedelta(days=4)  # this will never fail
#         last_day_of_month = last_day_of_month - timedelta(days=last_day_of_month.day)

#         # Filter the invoices within this month and sum the total_amount
#         total_sales_this_month = Invoice.objects.filter(
#             issued_at__date__range=(first_day_of_month, last_day_of_month),
#             paid=True
#         ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0  # Default to 0 if no sales

#         return Response({"total_sales_this_month": total_sales_this_month})


# class CustomerAnalysisView(APIView):
#     def get(self, request, format=None):
#         # Getting the date one month ago from today
#         one_month_ago = timezone.now() - timedelta(days=30)

#         # Filtering invoices from the past month and extracting the hour from the timestamp
#         customer_data = Invoice.objects.filter(issued_at__gte=one_month_ago).annotate(
#             hour_of_day=ExtractHour('issued_at')
#         ).values('hour_of_day').annotate(
#             average_customer_count=Avg('id')
#         ).order_by('hour_of_day')

#         analysis_result = defaultdict(int)
#         for entry in customer_data:
#             hour = entry['hour_of_day']
#             average_count = round(entry['average_customer_count']) 
#             analysis_result[hour] = average_count

#         return Response(analysis_result)




# import json
# from rest_framework.views import APIView
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# from rest_framework import generics
# from . import models, serializers
# from .models import Tag  # Import the Tag model
# from .serializers import TagSerializer  # Import the Tag serializer
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
# from rest_framework import status
# from .models import UserSession
# from .serializers import UserSessionSerializer
# from django.utils.crypto import get_random_string
# from .serializers import InvoiceSerializer
# from rest_framework.decorators import api_view
# from .models import Invoice
# from django.utils import timezone
# import datetime
# from .models import MenuItem
# from django.db.models import F, Sum, Count, IntegerField
# from django.db.models.functions import Cast
# from django.contrib.postgres.aggregates import ArrayAgg
# from django.db.models.fields.json import KeyTextTransform
# from django.db.models import OuterRef, Subquery, IntegerField
# from django.db.models.functions import Coalesce
# from collections import defaultdict
# from operator import itemgetter
# from collections import Counter
# from django.utils import timezone
# from datetime import timedelta, datetime
# from django.db.models.functions import ExtractWeekDay, ExtractHour
# from django.db.models.functions import ExtractHour
# from django.db.models import Count, Avg
# from .models import UserProfile, UserTagCount
# from .models import UserProfile
# from .serializers import MenuItemSerializer

import json
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import generics
from . import models, serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .models import UserSession, UserProfile, UserTagCount, Invoice, MenuItem, Tag
from django.utils.crypto import get_random_string
from .serializers import InvoiceSerializer, MenuItemSerializer, UserSessionSerializer, TagSerializer 
from rest_framework.decorators import api_view
from django.utils import timezone
from collections import defaultdict, Counter
from datetime import timedelta
from django.db.models.functions import ExtractHour
from django.db.models import Avg, Sum



# Create your views here.
class PlaceList(generics.ListCreateAPIView):
    serializer_class = serializers.PlaceSerializer

    def get_queryset(self):
        return models.Place.objects.filter(owner_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PlaceDetailSerializer
    queryset = models.Place.objects.all()

class CategoryList(generics.CreateAPIView):
    serializer_class = serializers.CategorySerializer

class CategoryDetail(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class MenuItemList(generics.CreateAPIView):
    serializer_class = serializers.MenuItemSerializer

class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = serializers.MenuItemSerializer
    queryset = models.MenuItem.objects.all()

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def create_payment_intent(request):
    data = json.loads(request.body)

    # Create the order as before
    order = models.Order.objects.create(
        place_id=data['place'],
        table=data['table'],
        detail=json.dumps(data['detail']),
        amount=data['amount'],
        session_id=data.get('sessionId'),  # Assume sessionId is passed correctly
        email=data['email'],  # Save email with the order
    )

    # Find or create the user profile for the email associated with the order
    user_profile, created = UserProfile.objects.get_or_create(email=data['email'])

    # Process each item in the order to update tag counts
    for item in data['detail']:
        menu_item_id = item['id']
        menu_item = MenuItem.objects.get(id=menu_item_id)
        # For each tag associated with this menu item, update the count in UserTagCount
        for tag in menu_item.tags.all():
            # Get or create a UserTagCount object for this tag and user profile
            user_tag_count, created = UserTagCount.objects.get_or_create(
                user_profile=user_profile, tag=tag)
            user_tag_count.count += 1  # Increment the count
            user_tag_count.save()  # Save the changes

    return JsonResponse({
        "success": True,
        "order": order.id,
    })

    
@csrf_exempt
def confirmPayment(request):
    try:
        data = json.loads(request.body)
        session_id = data.get('sessionId')

        # Find the corresponding UserSession and set it to inactive
        user_session = UserSession.objects.get(session_id=session_id)
        user_session.is_active = False
        user_session.save()

        return JsonResponse({"success": True, "message": "Payment confirmed and session updated."})

    except UserSession.DoesNotExist:
        return JsonResponse({"success": False, "error": "Session not found."})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})


class OrderList(generics.ListAPIView):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return models.Order.objects.filter(place__owner_id=self.request.user.id, place_id=self.request.GET.get('place'))

class OrderDetail(generics.UpdateAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()

class TagList(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
class TagCreate(CreateAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    
    
class TagDelete(APIView):
    """
    Delete a specific tag.
    """
    def delete(self, request, pk, format=None):
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class CreateSessionView(APIView):
    def post(self, request):
        email = request.data.get('email')
        table = request.data.get('table')  # Get the table number from the request

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not table:
            return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Logic to create a session and sessionId including the table number
        session = UserSession.create_session_for_email(email, table)
        serializer = UserSessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckSessionView(APIView):
    def post(self, request):
        table = request.data.get('table')  # Get the table number from the request

        if not table:
            return Response({"error": "Table number is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check for any active sessions for the given table
        active_sessions = UserSession.objects.filter(table=table, is_active=True)

        if active_sessions.exists():
            sessions_data = [{"session_id": session.session_id, "email": session.email} for session in active_sessions]
            return Response({
                "active_sessions": True,
                "sessions": sessions_data,
                "message": "Active sessions found for this table."
            }, status=status.HTTP_200_OK)
        else:
            return Response({"active_sessions": False}, status=status.HTTP_200_OK)


class GenerateInvoiceIDView(APIView):
    def get(self, request, format=None):
        # Generate a unique invoice ID
        invoice_id = get_random_string(length=12)  # Adjust the length as needed
        return Response({'invoice_id': invoice_id})
    
class CreateInvoiceView(APIView):
    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InvoiceListView(generics.ListAPIView):
    serializer_class = serializers.InvoiceSerializer

    def get_queryset(self):
        return models.Invoice.objects.all()




@api_view(['PUT'])
def update_invoice_status(request, invoice_id):
    try:
        invoice = Invoice.objects.get(invoice_number=invoice_id)  # Use invoice_number to get the Invoice
        invoice_data = request.data

        invoice.paid = invoice_data.get('paid', invoice.paid)
        invoice.save()

        return Response({'success': True, 'message': 'Invoice status updated.'})

    except Invoice.DoesNotExist:
        return Response({'success': False, 'error': 'Invoice not found.'}, status=404)

    except Exception as e:
        return Response({'success': False, 'error': str(e)}, status=500)




class PopularMenuItemThisWeek(APIView):
    def get(self, request, format=None):
        one_week_ago = timezone.now() - timedelta(days=7)
        
        # Fetch all invoices from the last week that were paid
        invoices = Invoice.objects.filter(issued_at__gte=one_week_ago, paid=True)
        
        # Initialize a Counter to count the quantities of each MenuItem
        item_counter = Counter()
        
        # Iterate over invoices and update the counter for each item
        for invoice in invoices:
            for item in invoice.items:  # Assuming that items is a list of dicts with 'id' and 'quantity' keys
                item_id = item.get('id')
                quantity = item.get('quantity', 1)  # Default to 1 if quantity is not specified
                item_counter[item_id] += quantity
        
        # Get the top 20 items by quantity ordered
        top_items = item_counter.most_common(20)
        
        # Extract the item IDs
        top_item_ids = [item[0] for item in top_items]

        # Retrieve the corresponding MenuItem objects for these IDs
        menu_items = MenuItem.objects.filter(id__in=top_item_ids).in_bulk()

        # Serialize the menu items
        serialized_data = serializers.MenuItemSerializer(
            [menu_items[item_id] for item_id in top_item_ids if item_id in menu_items],
            many=True
        ).data

        # Add the quantity ordered to the serialized data
        for item_data in serialized_data:
            item_id = item_data['id']
            item_data['ordered_quantity'] = item_counter[item_id]

        return Response(serialized_data)

        
class TotalSalesToday(APIView):
    def get(self, request, format=None):
        today = timezone.now().date()
        total_sales = models.Invoice.objects.filter(
            issued_at__date=today, 
            paid=True
        ).aggregate(Sum('total_amount'))

        return Response({"total_sales": total_sales['total_amount__sum'] or 0})
    
    
class TotalSalesThisWeek(APIView):
    def get(self, request, format=None):
        # Define the start of the week (e.g., Monday)
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=7)

        # Filter the invoices within this week and sum the total_amount
        total_sales_this_week = Invoice.objects.filter(
            issued_at__date__range=(start_of_week, end_of_week),
            paid=True
        ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0  # Default to 0 if no sales

        return Response({"total_sales_this_week": total_sales_this_week})

class TotalSalesThisMonth(APIView):
    def get(self, request, format=None):
        today = timezone.now().date()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=28) + timedelta(days=4)  # this will never fail
        last_day_of_month = last_day_of_month - timedelta(days=last_day_of_month.day)

        # Filter the invoices within this month and sum the total_amount
        total_sales_this_month = Invoice.objects.filter(
            issued_at__date__range=(first_day_of_month, last_day_of_month),
            paid=True
        ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0  # Default to 0 if no sales

        return Response({"total_sales_this_month": total_sales_this_month})


class CustomerAnalysisView(APIView):
    def get(self, request, format=None):
        # Getting the date one month ago from today
        one_month_ago = timezone.now() - timedelta(days=30)

        # Filtering invoices from the past month and extracting the hour from the timestamp
        customer_data = Invoice.objects.filter(issued_at__gte=one_month_ago).annotate(
            hour_of_day=ExtractHour('issued_at')
        ).values('hour_of_day').annotate(
            average_customer_count=Avg('id')
        ).order_by('hour_of_day')

        analysis_result = defaultdict(int)
        for entry in customer_data:
            hour = entry['hour_of_day']
            average_count = round(entry['average_customer_count']) 
            analysis_result[hour] = average_count

        return Response(analysis_result)


class UserFoodRecommendationView(APIView):
    def get(self, request, format=None):
        user_email = request.query_params.get('email')
        if not user_email:
            return Response({"error": "Email query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fetch the user profile using the provided email
            user_profile = UserProfile.objects.get(email=user_email)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Get recommended menu items for the user by calling the method on the user_profile instance
        recommendations = user_profile.recommend_menu_food_items()
        
        # Serialize the recommended items
        serializer = MenuItemSerializer(recommendations, many=True)
        
        # Return the serialized data
        return Response(serializer.data)
    
class UserDrinkRecommendationView(APIView):
    def get(self, request, format=None):
        user_email = request.query_params.get('email')
        if not user_email:
            return Response({"error": "Email query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fetch the user profile using the provided email
            user_profile = UserProfile.objects.get(email=user_email)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Get recommended menu items for the user by calling the method on the user_profile instance
        recommendations = user_profile.recommend_menu_drink_items()
        
        # Serialize the recommended items
        serializer = MenuItemSerializer(recommendations, many=True)
        
        # Return the serialized data
        return Response(serializer.data)
    
    
class ComboMealRecommendationView(APIView):
    def get(self, request, format=None):
        # Get the user's email from query parameters
        user_email = request.query_params.get('email')

        if not user_email:
            return Response({"error": "Email query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the user's profile
            user_profile = UserProfile.objects.get(email=user_email)
            # Get combo meal recommendations, now requesting up to 5 combos
            combo_meals = user_profile.recommend_combo_meals(top_n=5)  # Updated top_n to 5

            # Prepare the data for the response
            combo_meals_data = []
            for food_item, drink_item in combo_meals:
                food_data = MenuItemSerializer(food_item).data
                drink_data = MenuItemSerializer(drink_item).data
                combo_meals_data.append({
                    'food': food_data,
                    'drink': drink_data,
                })

            return Response(combo_meals_data)

        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




