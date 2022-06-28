from app.models import Medicine, Profile, Orders, Review
from rest_framework import serializers

class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
