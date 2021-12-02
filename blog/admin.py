from django.contrib import admin
from .models import Post,Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['id','name','meta_title']
    list_filter = ['created_at','updated_at']
    list_display_links = ['id','name']
    search_fields = ['name','id']
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
