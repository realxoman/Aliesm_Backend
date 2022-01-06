from django.db import models
from django.db.models.fields import DateTimeField
from aliesm_back_project.settings import LANGUAGE_CODE
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxLengthValidator
# Create your models here.
# ------------------ Images Path ------------------
def posts_thumb_path(instance, filename):
    return 'posts/images/{0}'.format(filename)
# ------------------ /Images Path ------------------

lang_choice = (
    ('persian', 'persian'),
    ('english', 'english')
)

class General(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد',null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی',null=True)
    language_field = models.CharField(max_length=256,blank=True,null=True,choices=lang_choice,verbose_name='زبان این محتوا')
    
    class Meta:
        abstract = True

    def get_created_at(self):
        return self.created_at.strftime("%H:%M - %Y/%m/%d")
    get_created_at.short_description = 'تاریخ ایجاد'

    def get_updated_at(self):
        return self.updated_at.strftime("%H:%M - %Y/%m/%d")
    get_updated_at.short_description = 'آخرین بروزرسانی'

class Seo(models.Model):
    slug = models.CharField(verbose_name="پیوند یکتا", max_length=60, \
        null=True)
    meta_title = models.CharField(verbose_name="meta title (SEO)", max_length=60, \
        null=True, help_text="حداکثر 60 کاراکتر")
    meta_description = models.TextField(verbose_name="meta description (SEO)", \
        validators=[MaxLengthValidator(170)], null=True, help_text="حداکثر 170 کاراکتر")

    class Meta:
        abstract = True

class Post(General,Seo):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    featured_image = models.ImageField(upload_to=posts_thumb_path,blank=True,null=True)
    content = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = '   Posts'
        verbose_name = 'Post'
        
class Comment(General):
    comments = models.ForeignKey("Comment", on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE,blank=True,null=True)
    username = models.CharField(max_length=256, blank=True, null=True)
    usermail = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.username + " " + str(self.id)
    
    def __unicode__(self):
        return self.username + " " + str(self.id)

    class Meta:
        verbose_name_plural = '   Comments'
        verbose_name = 'Comment'
        
        