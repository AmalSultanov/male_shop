from django.contrib import admin
from users.models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'country', 'email']
    list_filter = ['first_name', 'last_name', 'phone', 'email', 'country']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
