from django.db import models
from model_utils import Choices


# Create your models here.
class IngredientModel(models.Model):
    QUANTITY_NAME_CHOICES = Choices(
        ('g', 'г'),
        ('ml', 'мл'),
        ('tableSpoon', 'ст. ложка'),
        ('teaSpoon', 'ч. ложка'),
        ('pinch', 'дрібка'),
        ('unit', 'одиниць(-я)')
    )

    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    quantity_unit = models.CharField(max_length=10, choices=QUANTITY_NAME_CHOICES, default=QUANTITY_NAME_CHOICES.unit)

    def get_quantity_unit_display(self):
        return dict(IngredientModel.QUANTITY_NAME_CHOICES)[self.quantity_unit]

    class Meta:
        ordering = ['name']
        db_table = 'ingredient'
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'
        unique_together = ['name', 'quantity', 'quantity_unit']

    def __str__(self):
        return f'{self.name}, {self.quantity} {dict(IngredientModel.QUANTITY_NAME_CHOICES)[self.quantity_unit]}'


class ReceiptModel(models.Model):
    RECEIPT_TYPE_CHOICES = Choices(
        ('desert', 'Солодощі'),
        ('cake', 'Торти і пляцки'),
        ('cookie', 'Печиво'),
        ('bakery', 'Випічка'),
        ('other', 'Інше'),
    )

    title = models.CharField(max_length=50, unique=True)
    cooking_description = models.TextField()
    type = models.CharField(max_length=6, choices=RECEIPT_TYPE_CHOICES, default=RECEIPT_TYPE_CHOICES.other)
    ingredients = models.ManyToManyField(IngredientModel)

    class Meta:
        ordering = ['title']
        db_table = 'receipt'
        verbose_name = 'receipt'
        verbose_name_plural = 'receipts'

    def __str__(self):
        return self.title
