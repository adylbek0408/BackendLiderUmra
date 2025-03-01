from rest_framework import serializers
from .models import Manager, Client


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'user', 'telegram_id', 'phone']


class ClientSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'full_name', 'phone', 'country', 'city', 'package',
                  'status', 'manager', 'description', 'created_at', 'updated_at', 'description']


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['full_name', 'phone', 'country', 'city', 'package']
