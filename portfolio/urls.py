from django.urls import path
from .views import PortfolioListAPIView,PortfolioDetailAPIView
app_name = "portfolio"
urlpatterns = [
     path('', PortfolioListAPIView.as_view(),name="Portfolio"),
     path('detail/', PortfolioDetailAPIView.as_view(),name="Portfolio_details"),
]