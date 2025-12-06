from django.contrib import admin
from .models import Role, All_User, Admin, product_details, product_material, acc_details, operator_details, material_type, Machine, company, programer_details, Qa_details

# Register your models here.

admin.site.register(Admin)

admin.site.register(Role)

admin.site.register(All_User)

admin.site.register(company)

admin.site.register(operator_details)

admin.site.register(material_type)

admin.site.register(Machine)

admin.site.register(product_details)

admin.site.register(product_material)

admin.site.register(programer_details)

admin.site.register(Qa_details)

admin.site.register(acc_details)




