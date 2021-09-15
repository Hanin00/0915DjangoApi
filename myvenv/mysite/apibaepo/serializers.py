from rest_framework import serializers
from .models import Lift, Liftcheck


class LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = '__all__'


class LiftModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = ['lift_name', 'address', 'lift_status']

    lift_name = serializers.CharField(max_length=45)
    address = serializers.CharField(max_length=80)
    lift_status = serializers.CharField(max_length=45)



