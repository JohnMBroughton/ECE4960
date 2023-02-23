from django.contrib import admin
from dashboard.models import RFID
from dashboard.models import LotSize
# Register your models here.

# Admin site
# Databases
class C02Admin(admin.ModelAdmin):
    list_display = ('Lot','RFID')
    list_filter = ('Lot',)
admin.site.register(RFID, C02Admin)

class LotSizesAdmin(admin.ModelAdmin):
    list_display=('name','num_spaces')
admin.site.register(LotSize,LotSizesAdmin)