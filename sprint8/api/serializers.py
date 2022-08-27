from dataclasses import field
from rest_framework import serializers
from .models import Prestamo, Cuenta, Direccion, Cliente, Tarjeta


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"


class CuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"


class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"
