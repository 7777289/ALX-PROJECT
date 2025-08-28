# In apartments/urls.py
from django.urls import path
from .views import ApartmentListCreateView, ApartmentDetailView, MyApartmentListView

urlpatterns = [
    path('', ApartmentListCreateView.as_view(), name='apartment-list-create'),
    path('<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    path('my-apartments/', MyApartmentListView.as_view(), name='my-apartments'), # New URL
]