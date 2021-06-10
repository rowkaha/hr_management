from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Staffs, Office, Branch, Department, Designation, Shift

# Register your models here.
# class UserModel(UserAdmin):
#     pass
admin.site.register(CustomUser)
admin.site.register(Staffs)
admin.site.register(Office)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Shift)







