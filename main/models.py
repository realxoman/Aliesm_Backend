from django.db import models
from django.db.models.fields import DateField
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import Seo,General
# Create your models here.

# ------------------ Images Path ------------------
def Homefiles(instance, filename):
    return 'home/{0}'.format(filename)
# ------------------ /Images Path ------------------

class Setting(General,Seo):
    env_name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Enviorment Name")
    #Hero First
    name_of_site = models.CharField(max_length=50,null=True,blank=True,default="علی اسمعیلی",verbose_name="Site Name")
    slang = models.CharField(max_length=50,null=True,blank=True,default="برنامه نویس و تولید کننده محتوا",verbose_name="Slang of your site")
    content = RichTextUploadingField(null=True,blank=True,verbose_name="Content Of the Hero Section")
    avatar = models.ImageField(upload_to=Homefiles, null=True,blank=True,verbose_name="Avatar Image")
    cv = models.FileField(upload_to=Homefiles, null=True,blank=True,verbose_name="Your CV File")
    
    #Hero Second
    info_title1 = models.CharField(max_length=50,null=True,blank=True,verbose_name="Information Title 1")
    info_content1 = models.TextField(null=True,blank=True,verbose_name="Information Content 1")
    info_title2 = models.CharField(max_length=50,null=True,blank=True,verbose_name="Information Title 2")
    info_content2 = models.TextField(null=True,blank=True,verbose_name="Information Content 2")
    info_title3 = models.CharField(max_length=50,null=True,blank=True,verbose_name="Information Title 3")
    info_content3 = models.TextField(null=True,blank=True,verbose_name="Information Content 3")
    info_title4 = models.CharField(max_length=50,null=True,blank=True,verbose_name="Information Title 4")
    info_content4 = models.TextField(null=True,blank=True,verbose_name="Information Content 4")
    
    #Hero Third
    customers_title = models.CharField(max_length=50,null=True,blank=True,verbose_name="Customers Title")
    customers_num = models.IntegerField(null=True,blank=True,verbose_name="Customers Number")
    years_title = models.CharField(max_length=50,null=True,blank=True,verbose_name="Experience Years")
    years_num = models.IntegerField(null=True,blank=True,verbose_name="Experience Years Number")
    certificates_title = models.CharField(max_length=50,null=True,blank=True,verbose_name="Certificate Title")
    certificates_num = models.IntegerField(null=True,blank=True,verbose_name="Certificate Numbers")
    tea_title = models.CharField(max_length=50,null=True,blank=True,verbose_name="Tea Title")
    tea_num = models.IntegerField(null=True,blank=True,verbose_name="Tea Numbers")
    
    #Hero Fourth
    video_cv = models.URLField(max_length=200,null=True,blank=True,verbose_name="Video CV Link")
    video_cv_image = models.ImageField(upload_to=Homefiles, null=True,blank=True,verbose_name="Video CV Image")
    
    
    class Meta:
        verbose_name = ("Setting")
        verbose_name_plural = (" Settings")

    def __str__(self):
        return self.env_name

class Contact(General):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Name Of User")
    email = models.EmailField(max_length=50,null=True,blank=True,verbose_name="Email of User")
    subject = models.CharField(max_length=50,null=True,blank=True,verbose_name="Subject Of message")
    content = RichTextUploadingField(null=True,blank=True,verbose_name="Message")
    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.name
    
class Educations(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Name of institute")
    time = models.CharField(max_length=50,null=True,blank=True,verbose_name="Years of Education")
    place = models.CharField(max_length=50,null=True,blank=True,verbose_name="Institute location")
    btn_text = models.CharField(max_length=50,null=True,blank=True,verbose_name="Button Title")
    btn_link = models.URLField(max_length=50,null=True,blank=True,verbose_name="Button URL")
    order = models.PositiveSmallIntegerField(null=True, default=0,verbose_name="Order Number")
    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")
        ordering = ["order"]
    def __str__(self):
        return self.name
    
class Experiences(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Name of Company")
    time = models.CharField(max_length=50,null=True,blank=True,verbose_name="Years of Experience")
    place = models.CharField(max_length=50,null=True,blank=True,verbose_name="Company location")
    btn_text = models.CharField(max_length=50,null=True,blank=True,verbose_name="Button Title")
    btn_link = models.URLField(max_length=50,null=True,blank=True,verbose_name="Button URL")
    order = models.PositiveSmallIntegerField(null=True, default=0,verbose_name="Order Number")
    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Experiences")
        ordering = ["order"]
    def __str__(self):
        return self.name

class Certificates(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Name Of Certificate")
    issuer = models.CharField(max_length=50,null=True,blank=True,verbose_name="Name of Institute")
    time_of_issue = models.DateField(null=True,blank=True,verbose_name="Time of Issue")
    expired_time = models.DateField(null=True,blank=True,verbose_name="Time Of Expiration")
    logo = models.ImageField(upload_to=Homefiles, null=True,blank=True,verbose_name="Logo Of Institute")
    link_cert = models.URLField(max_length=50,null=True,blank=True,verbose_name="Link Of Certificate")
    order = models.PositiveSmallIntegerField(null=True, default=0,verbose_name="Order Number")
    class Meta:
        verbose_name = ("Certificate")
        verbose_name_plural = ("Certificates")
        ordering = ["order"]
    def __str__(self):
        return self.name
    
class Skills(General,models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Name of Skill")
    percent = models.CharField(max_length=50,null=True,blank=True,verbose_name="Percentage of Skill Experience")
    order = models.PositiveSmallIntegerField(null=True, default=0,verbose_name="Order Number")
    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")
        ordering = ["order"]
    def __str__(self):
        return self.name
    
class Pages(Seo,General):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE,blank=True,null=True,verbose_name="Author of page")
    name = models.CharField(max_length=256, blank=True, null=True,verbose_name="Name of Page")
    featured_image = models.ImageField(upload_to=Homefiles,blank=True,null=True,verbose_name="Thumbnail of page")
    content = RichTextUploadingField(null=True,blank=True,verbose_name="Content of Page")
    order = models.PositiveSmallIntegerField(null=True, default=0,verbose_name="Order Number")
    class Meta:
        verbose_name = ("Page")
        verbose_name_plural = ("Pages")
        ordering = ["order"]
    def __str__(self):
        return self.name