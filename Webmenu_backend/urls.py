
import re
from django.contrib import admin
from django.urls import path,include,re_path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    
    path('api/places/', views.PlaceList.as_view()),
    
    path('api/places/<pk>', views.PlaceDetail.as_view()),

    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<pk>', views.CategoryDetail.as_view()),

    path('api/menu_items/', views.MenuItemList.as_view()),
    path('api/menu_items/<pk>', views.MenuItemDetail.as_view()),

    path('api/create_payment_intent/', views.create_payment_intent),

    path('api/orders/', views.OrderList.as_view()),
    path('api/orders/<pk>', views.OrderDetail.as_view()),
    
    path('api/tags/', views.TagList.as_view(), name='tags'),
    path('api/tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('api/tags/<int:pk>/', views.TagDelete.as_view(), name='delete_tag'),
    
    path('api/sessions/', views.CreateSessionView.as_view(), name='session-create'),
    
    path('api/confirm_payment/', views.confirmPayment, name='confirm_payment'),
    
    path('api/check_session/', views.CheckSessionView.as_view(), name='check_session'),
    
    path('api/generate-invoice-id/', views.GenerateInvoiceIDView.as_view(), name='generate-invoice-id'),
    path('api/create-invoice/', views.CreateInvoiceView.as_view(), name='create-invoice'),
    
    path('api/invoices/', views.InvoiceListView.as_view(), name='invoice-list'),
    
    path('api/update-invoice/<str:invoice_id>/', views.update_invoice_status, name='update-invoice-status'),
    
    path('api/popular-item-this-week/', views.PopularMenuItemThisWeek.as_view(), name='popular-item-this-week'),
    path('api/total-sales-today/', views.TotalSalesToday.as_view(), name='total-sales-today'),
    
    path('api/total-sales-this-week/',views.TotalSalesThisWeek.as_view(), name='total-sales-this-week'),
    path('api/total-sales-this-month/', views.TotalSalesThisMonth.as_view(), name='total-sales-this-month'),
    
    path('api/customer-analysis/', views.CustomerAnalysisView.as_view(), name='customer-analysis'),
    
    path('api/food-recommendations/', views.UserFoodRecommendationView.as_view(), name='recommended-food-items'),
    path('api/drink-recommendations/', views.UserDrinkRecommendationView.as_view(), name='recommended-drink-items'),
    path('api/combo-recommendations/', views.ComboMealRecommendationView.as_view(), name='recommended-combo-items'),
    
]
