from django.contrib import admin
from dashboard.models import RFID
from dashboard.models import LotSize
# Register your models here.

# Admin site
# Databases
class RFIDAdmin(admin.ModelAdmin):
    list_display = ('Lot','RFID')
    list_filter = ('Lot',)
admin.site.register(RFID, RFIDAdmin)

class LotSizesAdmin(admin.ModelAdmin):
    list_display=('name','num_spaces','percentage_full')
admin.site.register(LotSize,LotSizesAdmin)