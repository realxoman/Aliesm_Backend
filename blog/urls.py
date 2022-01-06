from django.urls import path
from .views import PostListAPIView,PostDetailAPIView,CommentListCreateAPIView

app_name = "blog"
urlpatterns = [
    path('', PostListAPIView.as_view(),name="settings"),
    path('detail/', PostDetailAPIView.as_view(),name="settings"),
    path('comment/', CommentListCreateAPIView.as_view(),name="settings"),
]