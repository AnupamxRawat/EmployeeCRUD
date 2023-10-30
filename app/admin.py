from django.contrib import admin
from .models import Emoplyee,Position
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('FullName','emp_code','mobile')

class PositionAdmin(admin.ModelAdmin):
    list_display=('title',)    

admin.site.register(Emoplyee,EmployeeAdmin)
admin.site.register(Position,PositionAdmin)    