from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'email', 'phone', 'message', 'created_at')
    search_fields = ('firstname', 'email', 'phone')

# admin.site.register(CustomUser)