from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User, Account
from account.forms import UserAdminCreationForm, UserAdminChangeForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    search_fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm


    list_display = ['email', 'phone', 'first_name', 'last_name']
    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'email', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_seller')}),
        ('Dates', {'fields': ('date_joined', 'last_loged')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'phone', 'password', 'password_2', 'is_active', 'is_staff', 'is_seller')
        }),
    )

    ordering = ['email']


admin.site.register(User, UserAdmin)


class UserAccount(admin.ModelAdmin):
    list_display = ['user_email', 'address', 'city', 'state', 'country']

    def user_email(self, obj):
        return obj.user.email
    user_email.admin_order_field = 'user__email'

admin.site.register(Account, UserAccount)