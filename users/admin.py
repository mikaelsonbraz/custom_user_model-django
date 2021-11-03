from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("bio", "idade",)}),
    )
