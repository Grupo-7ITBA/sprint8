from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsEmployee
from rest_framework.permissions import AllowAny
from .models import Prestamo, Cuenta, Direccion, Tarjeta, Cliente
from .serializers import PrestamoSerializer, CuentasSerializer, DireccionesSerializer, SucursalSerializer, ClienteSerializer, TarjetaSerializer
# Create your views here.


class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all()

    def get_queryset(self):
        queryset = Prestamo.objects.all()
        sucursal_id = self.request.query_params.get('sucursal_id', None)
        if sucursal_id is not None:
            clientes = Cliente.objects.filter(branch_id=sucursal_id)
            queryset = queryset.filter(customer_id__in=clientes)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    customer_id=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            self.permission_classes = [IsEmployee]
        return super().get_permissions()


class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    # public api
    permission_classes = [AllowAny]
    serializer_class = SucursalSerializer
    queryset = Cuenta.objects.all()


class CuentasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CuentasSerializer

    def get_queryset(self):
        queryset = Cuenta.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(customer_id=customer_id)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    customer_id=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'partial_update':
            self.permission_classes = [IsEmployee]
        return super().get_permissions()


class DireccionesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DireccionesSerializer

    def get_queryset(self):
        queryset = Direccion.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(address_customer=customer_id)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    address_customer=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'partial_update':
            self.permission_classes = [IsEmployee]
        return super().get_permissions()


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        queryset = Cliente.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(customer_id=customer_id)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    customer_id=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'partial_update':
            self.permission_classes = [IsEmployee]
        return super().get_permissions()


class TarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TarjetaSerializer

    def get_queryset(self):
        queryset = Tarjeta.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(card_customer=customer_id)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    card_customer_id=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'partial_update':
            self.permission_classes = [IsEmployee]
        return super().get_permissions()
