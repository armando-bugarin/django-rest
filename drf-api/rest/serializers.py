from rest_framework import serializers
from .models import Rest

class RestSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id","owner","name","description","created_at")
    model = Rest
