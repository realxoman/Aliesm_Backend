from django.contrib import admin
from .models import Post,Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    fieldsets = (
     ('Post Terms',{
         'fields': ('name','content')
     })  ,
     ('Post Meta',{
         'fields': ('featured_image','user')
     }),('SEO Terms',{
         'fields': ('meta_title','meta_description')
     }) 
    )
    add_fieldsets = (
     ('Post Terms',{
         'fields': ('name','content')
     })  ,
     ('Post Meta',{
         'fields': ('featured_image','user')
     }),('SEO Terms',{
         'fields': ('meta_title','meta_description')
     }) 
    )
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
