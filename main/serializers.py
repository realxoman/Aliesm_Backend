from rest_framework import serializers
from .models import Educations,Experiences,Contact,Certificates,Pages,Skills,Setting

class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields = '__all__'
        
class ExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = '__all__'
        
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
        
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'