from django.contrib import admin
from .models import Certificates,Contact,Educations,Experiences,Pages,Skills,settings
# Register your models here.

@admin.register(settings)
class settingsAdmin(admin.ModelAdmin):
    list_display =['env_name','name_of_site','slang']
    list_display_links = ['env_name']
    search_fields = ['env_name']
    fieldsets = (
        ('Enviorment Section',{
            'fields': ['language_field','env_name']
            }),
        
        #Hero First
        ('Hero First - Personal Details',{
            'fields': ('name_of_site','slang','content','avatar','cv')
            }),
        
        #Hero Second
        ('Hero Second - Info 1',{
            'fields': ('info_title1','info_content1')
            }),
        ('Hero Second - Info 2',{
            'fields': ('info_title2','info_content2')
            }),
        ('Hero Second - Info 3',{
            'fields': ('info_title3','info_content3')
            }),
        ('Hero Second - Info 4',{
            'fields': ('info_title4','info_content4')
            }),
        
        #Hero Third
        ('Hero Third - Customers',{
            'fields': ('customers_title','customers_num')
            }),
        ('Hero Third - Years',{
            'fields': ('years_title','years_num')
            }),
        ('Hero Third - Certificates',{
            'fields': ('certificates_title','certificates_num')
            }),
        ('Hero Third - Tea',{
            'fields': ('tea_title','tea_num')
            }),
        
        #Hero Fourth
        ('Hero Fourth - Video',{
            'fields': ('video_cv','video_cv_image')
            }),
        
        #SEO
        ('SEO Terms',{
         'fields': ('slug','meta_title','meta_description')
         }) 
                 )
    add_fieldsets = (
        ('Enviorment Section',{
            'fields': ('language_field','env_name')
            }),
        
        #Hero First
        ('Hero First - Personal Details',{
            'fields': ('name_of_site','slang','content','avatar','cv')
            }),
        
        #Hero Second
        ('Hero Second - Info 1',{
            'fields': ('info_title1','info_content1')
            }),
        ('Hero Second - Info 2',{
            'fields': ('info_title2','info_content2')
            }),
        ('Hero Second - Info 3',{
            'fields': ('info_title3','info_content3')
            }),
        ('Hero Second - Info 4',{
            'fields': ('info_title4','info_content4')
            }),
        
        #Hero Third
        ('Hero Third - Customers',{
            'fields': ('customers_title','customers_num')
            }),
        ('Hero Third - Years',{
            'fields': ('years_title','years_num')
            }),
        ('Hero Third - Certificates',{
            'fields': ('certificates_title','certificates_num')
            }),
        ('Hero Third - Tea',{
            'fields': ('tea_title','tea_num')
            }),
        
        #Hero Fourth
        ('Hero Fourth - Video',{
            'fields': ('video_cv','video_cv_image')
            }),
        
        #SEO
        ('SEO Terms',{
         'fields': ('slug','meta_title','meta_description')
         }) 
                 )

@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display =['name','issuer','time_of_issue','expired_time','order']
    list_filter = ['time_of_issue','expired_time']
    list_display_links = ['name']
    search_fields = ['name','issuer']
    fieldsets = (
     ('Certificate Terms',{
         'fields': ('language_field','name','issuer')
     }),
     ('Certificate Times',{
         'fields': ('time_of_issue','expired_time')
     }),
     ('Certificate Meta',{
         'fields': ('logo','link_cert')
     }),
    )
    add_fieldsets = (
     ('Certificate Terms',{
         'fields': ('language_field','name','issuer')
     }),
     ('Certificate Times',{
         'fields': ('time_of_issue','expired_time')
     }),
     ('Certificate Meta',{
         'fields': ('logo','link_cert','order')
     }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =['name','email','created_at']
    list_filter = ['created_at']
    list_display_links = ['name']
    search_fields = ['name','email']

@admin.register(Educations)
class EducationsAdmin(admin.ModelAdmin):
    list_display =['name','time','place','order']
    list_display_links = ['name']
    search_fields = ['name','place']
    fieldsets = (
        ('Short Details',{
            'fields': ('language_field','name','place','time')
            }),
        ('Details',{
            'fields': ('btn_text','btn_link','order')
            }),
                 )
    add_fieldsets = (
        ('Short Details',{
            'fields': ('language_field','name','place','time')
            }),
        ('Details',{
            'fields': ('btn_text','btn_link','order')
            }),
                 )

@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display =['name','time','place','order']
    list_display_links = ['name']
    search_fields = ['name','place']
    fieldsets = (
        ('Short Details',{
            'fields': ('language_field','name','place','time')
            }),
        ('Details',{
            'fields': ('btn_text','btn_link','order')
            }),
                 )
    add_fieldsets = (
        ('Short Details',{
            'fields': ('language_field','name','place','time')
            }),
        ('Details',{
            'fields': ('btn_text','btn_link','order')
            }),
                 )

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display =['id','name','meta_title']
    list_filter = ['created_at','updated_at']
    list_display_links = ['id','name']
    search_fields = ['name','id']
    fieldsets = (
     ('Post Terms',{
         'fields': ('language_field','name','content')
     })  ,
     ('Post Meta',{
         'fields': ('featured_image','user')
     }),('SEO Terms',{
         'fields': ('meta_title','meta_description')
     }) 
    )
    add_fieldsets = (
     ('Post Terms',{
         'fields': ('language_field','name','content')
     })  ,
     ('Post Meta',{
         'fields': ('featured_image','user')
     }),('SEO Terms',{
         'fields': ('slug','meta_title','meta_description')
     }) 
    )

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display =['name','percent','order']
    list_display_links = ['name']
    search_fields = ['name','percent']


