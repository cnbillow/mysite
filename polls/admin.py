from django.contrib import admin

# Register your models here.

from .models import MainManu,SecondaryManu,Article,Product,CustomerAppraise,FAQ,Consult

admin.site.register(MainManu)
admin.site.register(SecondaryManu)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(CustomerAppraise)
admin.site.register(FAQ)
admin.site.register(Consult)


admin.site.site_header = '后台管理系统'
