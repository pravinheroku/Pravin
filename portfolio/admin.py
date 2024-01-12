from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Contact)
# admin.site.register(Blogs)


class ContactDetails(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "description")
    search_fields = ("name", "email", "phonw_number")
    
admin.site.register(Contact, ContactDetails)

class BlogDetails(admin.ModelAdmin):
    list_display = ("title", "description", "authname", "img", "timeStamp")
    search_fields = ("title", "authname")
    
admin.site.register(Blogs, BlogDetails)