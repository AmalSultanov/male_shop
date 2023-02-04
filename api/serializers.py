from rest_framework import serializers
from items.models import ItemModel, CategoryModel, BrandModel, ColorModel, SizeModel, ItemTagModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['title_en', 'title_ru']


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = '__all__'


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'


class ItemTagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTagModel
        fields = '__all__'


class ItemModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    brand = BrandModelSerializer()
    sizes = CategoryModelSerializer(many=True)
    colors = CategoryModelSerializer(many=True)
    tags = CategoryModelSerializer(many=True)

    class Meta:
        model = ItemModel
        exclude = ['title_en', 'title_ru', 'short_description_en', 'short_description_ru',
                   'long_description_en', 'long_description_ru', 'wishlist']
