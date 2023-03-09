from django.db import models
from django.utils.html import format_html

# Create your models here.
class RFID(models.Model):
    Lot = models.CharField(max_length=200)
    RFID = models.IntegerField(default=0)
	#
class LotSize(models.Model):
    name = models.CharField(max_length=200)
    num_spaces = models.IntegerField(default=0)
    def percentage_full(self):
        if self.name and self.num_spaces:
            percentage = round((RFID.objects.filter(Lot=self.name).count() / self.num_spaces * 100),2)
        else:
            percentage = 0
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            percentage
        )