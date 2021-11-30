from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# ------------------ Images Path ------------------
def Homefiles(instance, filename):
    return 'home/{0}'.format(filename)
# ------------------ /Images Path ------------------

class settings(models.Model):
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
    videocv = models.CharField(max_length=50,null=True,blank=True)
    
    class Meta:
        verbose_name = ("Setting")
        verbose_name_plural = (" Settings")

    def __str__(self):
        return self.env_name

class Fee(models.Model):

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    subject = models.CharField(max_length=50,null=True,blank=True)
    content = RichTextUploadingField(null=True,blank=True)
    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.name