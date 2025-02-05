from django.contrib import admin
from .models import Driver,Guest,Category,Subcategory,Post
from import_export.admin import ExportActionMixin

# Register your models here.

class GuestAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('phone_number', 'uuid', 'role', 'name', 'surname', 'village', 'taluka', 'district', 'created_at')
    search_fields = ('phone_number', 'uuid', 'role', 'name', 'taluka',)
    list_filter = ('role', 'created_at')

class DriverAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user', 'license_number', 'vehicle_number', 'experience_years', 'aadhar_number', 'type_of_driver',)    
    search_fields = ('user', 'license_number', 'vehicle_number', 'aadhar_number',)

class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display=('category','category_link')
    search_fields=('category','category_link')

class SubCategroyAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=('subcategory','subcategory_link')
    search_fields=('subcategory','subcategory_link')

class PostAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display=('title','description','price','price_category','phone_no','whatsapp_no','taluka','village',)       
    search_fields=('title','description','price','price_category','phone_no','whatsapp_no','taluka','village',) 

admin.site.register(Guest, GuestAdmin)
admin.site.register(Driver, DriverAdmin)    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategroyAdmin)
admin.site.register(Post, PostAdmin)
