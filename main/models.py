from django.db import models
from django.db.models.fields import DateField
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import Seo,General
# Create your models here.

# ------------------ Images Path ------------------
def Homefiles(instance, filename):
    return 'home/{0}'.format(filename)
# ------------------ /Images Path ------------------

class settings(General,Seo):
    env_name = models.CharField(max_length=50,null=True,blank=True)
    #Hero First
    name_of_site = models.CharField(max_length=50,null=True,blank=True,default="علی اسمعیلی")
    slang = models.CharField(max_length=50,null=True,blank=True,default="برنامه نویس و تولید کننده محتوا")
    content = RichTextUploadingField(null=True,blank=True)
    avatar = models.ImageField(upload_to=Homefiles, null=True,blank=True)
    cv = models.FileField(upload_to=Homefiles, null=True,blank=True)
    
    #Hero Second
    info_title1 = models.CharField(max_length=50,null=True,blank=True)
    info_content1 = models.TextField(null=True,blank=True)
    info_title2 = models.CharField(max_length=50,null=True,blank=True)
    info_content2 = models.TextField(null=True,blank=True)
    info_title3 = models.CharField(max_length=50,null=True,blank=True)
    info_content3 = models.TextField(null=True,blank=True)
    info_title4 = models.CharField(max_length=50,null=True,blank=True)
    info_content4 = models.TextField(null=True,blank=True)
    
    #Hero Third
    customers_title = models.CharField(max_length=50,null=True,blank=True)
    customers_num = models.IntegerField(null=True,blank=True)
    years_title = models.CharField(max_length=50,null=True,blank=True)
    years_num = models.IntegerField(null=True,blank=True)
    certificates_title = models.CharField(max_length=50,null=True,blank=True)
    certificates_num = models.IntegerField(null=True,blank=True)
    tea_title = models.CharField(max_length=50,null=True,blank=True)
    tea_num = models.IntegerField(null=True,blank=True)
    
    #Hero Fourth
    video_cv = models.CharField(max_length=50,null=True,blank=True)
    video_cv_image = models.ImageField(upload_to=Homefiles, null=True,blank=True)
    
    
    class Meta:
        verbose_name = ("Setting")
        verbose_name_plural = (" Settings")

    def __str__(self):
        return self.env_name

class Contact(General):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    subject = models.CharField(max_length=50,null=True,blank=True)
    content = RichTextUploadingField(null=True,blank=True)
    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.name
    
class Educations(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    time = models.CharField(max_length=50,null=True,blank=True)
    place = models.CharField(max_length=50,null=True,blank=True)
    btn_text = models.CharField(max_length=50,null=True,blank=True)
    btn_link = models.URLField(max_length=50,null=True,blank=True)
    order = models.PositiveSmallIntegerField(null=True, default=0)
    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")
        ordering = ["order"]
    def __str__(self):
        return self.name
    
class Experiences(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    time = models.CharField(max_length=50,null=True,blank=True)
    place = models.CharField(max_length=50,null=True,blank=True)
    btn_text = models.CharField(max_length=50,null=True,blank=True)
    btn_link = models.URLField(max_length=50,null=True,blank=True)
    order = models.PositiveSmallIntegerField(null=True, default=0)
    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Experiences")
        ordering = ["order"]
    def __str__(self):
        return self.name

class Certificates(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    issuer = models.CharField(max_length=50,null=True,blank=True)
    time_of_issue = models.DateField(null=True,blank=True)
    expired_time = models.DateField(null=True,blank=True)
    logo = models.ImageField(upload_to=Homefiles, null=True,blank=True)
    link_cert = models.URLField(max_length=50,null=True,blank=True)
    order = models.PositiveSmallIntegerField(null=True, default=0)
    class Meta:
        verbose_name = ("Certificate")
        verbose_name_plural = ("Certificates")
        ordering = ["order"]
    def __str__(self):
        return self.name
    
class Skills(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    percent = models.CharField(max_length=50,null=True,blank=True)
    order = models.PositiveSmallIntegerField(null=True, default=0)
    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")
        ordering = ["order"]
    def __str__(self):
        return self.name
    
class Pages(Seo,General):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    featured_image = models.ImageField(upload_to=Homefiles,blank=True,null=True)
    content = RichTextUploadingField(null=True,blank=True)
    order = models.PositiveSmallIntegerField(null=True, default=0)
    class Meta:
        verbose_name = ("Page")
        verbose_name_plural = ("Pages")
        ordering = ["order"]
    def __str__(self):
        return self.name