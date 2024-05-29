from django.contrib import admin

# Register your models here.
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'email', 'phone', 'message', 'created_at')
    search_fields = ('firstname', 'email', 'phone')


# admin.site.register(User, UserAdmin)
# admin.site.register(CustomUser)
