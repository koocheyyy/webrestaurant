from rest_framework import serializers
from . import models

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['id', 'name']



class MenuItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = models.MenuItem
        fields = ('id', 'name', 'description', 'price', 'image', 'is_available', 'place', 'category', 'tags', 'is_drink')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        menu_item = models.MenuItem.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = models.Tag.objects.get_or_create(**tag_data)
            menu_item.tags.add(tag)
        return menu_item

    def update(self, instance, validated_data):
        instance.tags.clear()  # Clear existing tags
        tags_data = validated_data.pop('tags', [])
        for tag_data in tags_data:
            tag, created = models.Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return super().update(instance, validated_data)

class CategorySerializer(serializers.ModelSerializer):
  menu_items = MenuItemSerializer(many=True, read_only=True)

  class Meta:
    model = models.Category
    fields = ('id', 'name', 'menu_items', 'place')

class PlaceDetailSerializer(serializers.ModelSerializer):
  categories = CategorySerializer(many=True, read_only=True)
  
  class Meta:
    model = models.Place
    fields = ('id', 'name', 'image', 'font', 'color', 'number_of_tables', 'categories', 'tax_amount')

class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Place
    fields = ('id', 'name', 'image')

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Order
    fields = "__all__"
    
class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserSession
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = '__all__'