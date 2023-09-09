from django.contrib import admin
from receipt.models import ReceiptModel, IngredientModel


# Register your models here.
@admin.register(ReceiptModel)
class ReceiptModelFilter(admin.ModelAdmin):
    filter_horizontal = ('ingredients',)


admin.site.register(IngredientModel)
