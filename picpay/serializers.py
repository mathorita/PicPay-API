import requests
from rest_framework import serializers
from .models import Transaction, User
from django.db import transaction as db_transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        sender = data['sender']
        receiver = data['receiver']
        value = data['value']

        if sender == receiver:
            raise serializers.ValidationError('You must send money to a different person!')
        if sender.user_type == 'L':
            raise serializers.ValidationError('Lojistas cannot send money!')
        if sender.wallet < value:
            raise serializers.ValidationError('Sender has insufficient funds!')
        return data

    def create(self, validated_data):
        sender = validated_data['sender']
        receiver = validated_data['receiver']
        value = validated_data['value']

        auth_response = requests.get('https://util.devi.tools/api/v2/authorize')
        if auth_response.status_code != 200 or auth_response.json().get("message") != "Autorizado":
            raise serializers.ValidationError("Transaction not authorized by external service.")

        with db_transaction.atomic():
            sender.wallet -= value
            receiver.wallet += value
            sender.save()
            receiver.save()
            transaction = Transaction.objects.create(**validated_data)

            notify_response = requests.post('https://util.devi.tools/api/v1/notify', json={
                'sender': sender.email,
                'receiver': receiver.email,
                'value': str(value),
            })


            return transaction
