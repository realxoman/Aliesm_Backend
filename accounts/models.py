from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

# Create your models here.

class User(AbstractUser):
    date_joined = models.DateTimeField(verbose_name="Register Time", auto_now_add=True, null=True)
    last_update = models.DateTimeField(verbose_name="Latest Update Time", auto_now=True, null=True)
    last_login = models.DateTimeField(verbose_name="Last Login", null=True, blank=True)
    
    is_manager = models.BooleanField(verbose_name="Manager", default=False,\
        help_text="Manager have full access")
        
    phone = models.CharField(verbose_name="PhoneNumber", max_length=11, unique=True, null=True, blank=True, \
        help_text="Enter with zero at first. 09...")

    email = models.EmailField(verbose_name="E-Mail", unique=True, null=True)

    REQUIRED_FIELDS = ['email']
    
    def get_date_joined(self):
        return self.date_joined.strftime("%H:%M - %Y/%m/%d")
    get_date_joined.short_description = 'Register Date & Time'

    def get_date_joined__date_only(self):
        return self.date_joined.strftime("%Y/%m/%d")

    def get_last_update(self):
        return self.last_update.strftime("%H:%M - %Y/%m/%d")
    get_last_update.short_description = 'Latest Update Date & Time'

    def get_last_login(self):
        if self.last_login:
            return self.last_login.strftime("%H:%M - %Y/%m/%d")
        return "Not login yet."
    get_last_login.short_description = 'Last Login'

    def __str__(self):
        return "%s - %s" % (self.username, self.get_full_name())

    
    class Meta:
        verbose_name_plural = '   Users'
        verbose_name = 'User'