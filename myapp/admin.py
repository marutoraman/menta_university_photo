from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from .models import University,Major,User

from .models import StudentUser,EditUser

# 不要なアカウントの非表示
admin.site.unregister(Group)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(Site)



# 必要なアカウントの表示設定
@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('username', 'email', 'user_type')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       )})
    )
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = []
    search_fields = ('email', 'username')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)
    
    
@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    fields = ('nickname', 'university_name', 'major_name')
    list_display = ('nickname', 'university_name', 'major_name')
    ordering = ('nickname',)
    
    
@admin.register(EditUser)
class EditUserAdmin(admin.ModelAdmin):
    fields = ('nickname', 'university_name')
    list_display = ('nickname', 'university_name')
    ordering = ('nickname',)
    
admin.site.register(University)
admin.site.register(Major)