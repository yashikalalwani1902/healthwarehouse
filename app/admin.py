from django.contrib import admin
from app.models import Profile, Medicine, Orders, Review
from django.contrib.admin.options import ModelAdmin

# Register your models here.
admin.site.register(Profile)

class MedicineAdmin(ModelAdmin):
    list_display = ['name','description','price','mfg_date','exp_date','cr_date']
    search_fields = ['name','description','price']
    list_filter = ["mfg_date", "exp_date",'cr_date']
    
admin.site.register(Medicine,MedicineAdmin)
admin.site.register(Orders)
admin.site.register(Review)

