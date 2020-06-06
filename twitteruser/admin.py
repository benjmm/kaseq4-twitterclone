from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import TwitterUserCreationForm, TwitterUserChangeForm
from .models import TwitterUser


class TwitterUserAdmin(UserAdmin):
    add_form = TwitterUserCreationForm
    form = TwitterUserChangeForm
    model = TwitterUser
    list_display = ['username', 'display_name', 'email', ]
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'display_name',
                           'email', 'password', 'following')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'display_name', 'email', 'password1',
                       'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(TwitterUser, TwitterUserAdmin)
