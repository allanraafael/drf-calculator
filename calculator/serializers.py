from rest_framework import serializers
from calculator import models


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Operation
        fields = ['parameter_a', 'parameter_b', 'symbol', 'result']


class GenericOperationSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()
    symbol = serializers.SerializerMethodField()
    operation_symbol = ''

    def get_result(self, obj):
        return eval(f'{obj.parameter_a} {self.operation_symbol} {obj.parameter_b}')

    def get_symbol(self, obj):
        return self.operation_symbol

    def create(self, validated_data):
        operation = self.Meta.model(**validated_data)
        operation.result = self.get_result(operation)
        operation.symbol = self.operation_symbol
        operation.save()
        return operation

    class Meta:
        model = models.Operation
        fields = ['parameter_a', 'parameter_b', 'symbol', 'result']


class AdditionSerializer(GenericOperationSerializer):
    operation_symbol = '+'

    class Meta(GenericOperationSerializer.Meta):
        model = models.Addition


class SubtractionSerializer(GenericOperationSerializer):
    operation_symbol = '-'

    class Meta(GenericOperationSerializer.Meta):
        model = models.Subtraction


class MultiplicationSerializer(GenericOperationSerializer):
    operation_symbol = '*'

    class Meta(GenericOperationSerializer.Meta):
        model = models.Multiplication


class FloorDivisionSerializer(GenericOperationSerializer):
    operation_symbol = '//'

    class Meta(GenericOperationSerializer.Meta):
        model = models.FloorDivision
