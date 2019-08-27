from rest_framework import serializers
from .models import Quote,Item
import copy

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id1", "name")



class QuoteSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = Quote
        fields = ("name", "price", "items")

    def create(self, validated_data) :
        items_data = validated_data.pop('items')
        quote = Quote.objects.create(**validated_data)
        for item_data in items_data :
            Item.objects.create(quote=quote, **item_data)
        return quote

    def update(self, instance, validated_data) :
        instance.name = validated_data['name']
        instance.price = validated_data['price']

        instance.save()

        item_ids = [item['id1'] for item in validated_data['items']]
        for item in instance.items.all() :
            if item.id not in item_ids :
                item.delete()

        # Create or update page instances that are in the request
        for item in validated_data['items'] :
                tmpItem = Item(id1=item['id1'], name=item['name'], quote=instance)
                tmpItem.save()

        return instance
