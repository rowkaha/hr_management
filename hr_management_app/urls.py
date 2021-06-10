
from django.contrib import admin
from django.urls import path, include
from hr_management_app import views, AdminViews
urlpatterns = [
    path('', views.ShowLoginPage, name='ShowLoginPage'),    
    path('doLogin', views.doLogin, name='doLogin'),
    path('get_user_details', views.get_user_details, name="get_user_details"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('admin_home', AdminViews.admin_home, name="admin_home"),
    # staff workout
    path('add_staff', AdminViews.add_staff.as_view(), name='add_staff'),
    path('manage_staff', AdminViews.manage_staff, name="manage_staff"),
    path('edit_staff/<str:staff_id>', AdminViews.edit_staff.as_view(), name="edit_staff"),
    path('delete_staff/<int:staff_id>', AdminViews.delete_staff, name="delete_staff"),
    # office workout
    path('add_office', AdminViews.add_office.as_view(), name="add_office"),
    path('manage_office', AdminViews.manage_office, name="manage_office"),
    path('edit_office/<str:office_id>', AdminViews.edit_office.as_view(), name="edit_office"),
    path('delete_office/<int:office_id>', AdminViews.delete_office, name="delete_office"),
    # branch workout
    path('manage_branch', AdminViews.manage_branch, name="manage_branch"),
    path('add_branch', AdminViews.add_branch.as_view(), name="add_branch"),
     path('edit_branch/<str:branch_id>', AdminViews.edit_branch.as_view(), name="edit_branch"),
    path('delete_branch/<int:branch_id>', AdminViews.delete_branch, name="delete_branch"),
    # manage department
    path('manage_department', AdminViews.manage_department, name="manage_department"),
    path('add_department', AdminViews.add_department.as_view(), name="add_department"),
    path('edit_department/<str:department_id>', AdminViews.edit_department.as_view(), name="edit_department"),
    path('delete_department/<int:department_id>', AdminViews.delete_department, name="delete_department"),
    # manage designation
    path('manage_designation', AdminViews.manage_designation, name="manage_designation"),
    path('add_designation', AdminViews.add_designation.as_view(), name="add_designation"),
    path('edit_designation/<str:designation_id>', AdminViews.edit_designation.as_view(), name="edit_designation"),
    path('delete_designation/<int:designation_id>', AdminViews.delete_designation, name="delete_designation"),
    # manage shift
    path('manage_shift', AdminViews.manage_shift, name="manage_shift"),
    path('delete_shift/<int:shift_id>', AdminViews.delete_shift, name="delete_shift"),
    path('add_shift', AdminViews.add_shift.as_view(), name="add_shift"),
    path('edit_shift/<str:shift_id>', AdminViews.edit_shift.as_view(), name="edit_shift"),








]
