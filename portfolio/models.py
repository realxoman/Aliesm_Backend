from django.db import models
from blog.models import Seo,General
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# ------------------ Images Path ------------------
def posts_thumb_path(instance, filename):
    return 'portfolio/images/{0}'.format(filename)
# ------------------ /Images Path ------------------

class Portfolio(General,Seo):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE,blank=True,null=True,verbose_name="Author User")
    name = models.CharField(max_length=256, blank=True, null=True,verbose_name="Title Of Portfolio")
    featured_image = models.ImageField(upload_to=posts_thumb_path,blank=True,null=True,verbose_name="Thumbnail Image")
    content = RichTextUploadingField(blank=True,null=True,verbose_name="Content Text")
    link = models.URLField(null=True,blank=True,verbose_name="URL of the Project")
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural = '   Projects'
        verbose_name = 'Projects'
