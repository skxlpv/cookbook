from rest_framework import serializers

from receipt.models import ReceiptModel, IngredientModel


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientModel
        fields = ['name', 'quantity', 'quantity_unit']


class ReceiptSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = ReceiptModel
        fields = ['title', 'cooking_description',
                  'type', 'ingredients']
