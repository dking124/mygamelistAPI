from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Game

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_staff')
    search_fields = ('email', 'username')
    #readonly_fields = ('date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class GameAdmin(admin.ModelAdmin):
    list_display = ('user', 'igdb_id', 'is_completed', 'rating', 'total_hours')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game, GameAdmin)