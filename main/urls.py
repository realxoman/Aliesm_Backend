from django.urls import path
from .views import settingsListAPIView,ContactListCreateAPIView,ResumeAPIView,PagesDetailAPIView
app_name = "main"

urlpatterns = [
    path('', settingsListAPIView.as_view(),name="settings"),
    path('contact/', ContactListCreateAPIView.as_view(),name="Contact"),
    path('cv/', ResumeAPIView.as_view(),name="cv"),
    path('pages/', PagesDetailAPIView.as_view(),name="Pages"),
]