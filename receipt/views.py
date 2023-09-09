from rest_framework import generics, mixins

from receipt.models import ReceiptModel
from receipt.serializers import ReceiptSerializer


class ReceiptView(generics.ListAPIView):
    serializer_class = ReceiptSerializer

    def get_queryset(self):
        queryset = ReceiptModel.objects.all()
        return queryset
