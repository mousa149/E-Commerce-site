from django.contrib import admin
from .models import Products,Order
# Register your models her

admin.site.site_header='E-commerce Site'
admin.site.site_title = 'ABC Shopping'
admin.site.index_title = 'manage abc shopping'



class Productadmin(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category = 'default')

    change_category_to_default.short_description= 'Default Category'
    list_display=('title','price','discount_price','category')
    search_fields=('title','category')
    actions = (change_category_to_default,)
    fields = ('title','price')
    list_editable=('price','category')
admin.site.register(Products,Productadmin)
admin.site.register(Order)