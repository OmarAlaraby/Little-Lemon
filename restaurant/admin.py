from django.contrib import admin
from .models import Restaurant , Chef , Awards , Customer ,Staff

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Chef)
admin.site.register(Awards)
admin.site.register(Customer)
admin.site.register(Staff)