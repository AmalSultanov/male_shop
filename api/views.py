from rest_framework.generics import ListAPIView

from api.serializers import ItemModelSerializer
from items.models import ItemModel


class ItemListAPIView(ListAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemModelSerializer
