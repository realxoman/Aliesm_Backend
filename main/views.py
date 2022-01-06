from django.db.models import query
from django.shortcuts import render
from .models import Educations,Experiences,Contact,Certificates,Pages,Skills,settings
from .serializers import CertificatesSerializer,ContactSerializer,EducationsSerializer,ExperiencesSerializer,PagesSerializer,settingsSerializer,SkillsSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

class settingsListAPIView(generics.ListAPIView):
    queryset = settings.objects.all()
    serializer_class = settingsSerializer
    
class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class PagesDetailAPIView(APIView):
    def get(self, request, format=None):
        req = request.data.get('id') or "1"
        queryset = get_object_or_404(Pages, id=req)
        serializer_class = PagesSerializer(instance=queryset)
        data = serializer_class.data
        return Response(data)

class ResumeAPIView(APIView):
    def get(self, request, format=None):
        #Certificates
        certificates = Certificates.objects.all()
        certificates_serilizer = CertificatesSerializer(certificates, many=True)
        #Educations
        educations = Educations.objects.all()
        educations_serilizer = EducationsSerializer(educations, many=True)
        #Experiences
        experiences = Experiences.objects.all()
        experiences_serilizer = ExperiencesSerializer(experiences, many=True)
        #Skills
        skills = Skills.objects.all()
        skills_serilizer = SkillsSerializer(skills, many=True)
        
        FinalResult = {
            "Certificates":certificates_serilizer.data,
            "Educations":educations_serilizer.data,
            "Experiences":experiences_serilizer.data,
            "Skills":skills_serilizer.data,
        }
        return Response(FinalResult)