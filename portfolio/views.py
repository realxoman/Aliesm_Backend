from django.shortcuts import render
from .models import Portfolio
from .serializers import PortfolioSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.


class PortfolioListAPIView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    
class PortfolioDetailAPIView(APIView):
    def get(self, request, format=None):
        req = request.data.get('id') or "1"
        queryset = get_object_or_404(Portfolio, id=req)
        serializer_class = PortfolioSerializer(instance=queryset)
        data = serializer_class.data
        return Response(data)