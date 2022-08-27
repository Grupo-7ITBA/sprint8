from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PrestamoViewSet, CuentasViewSet, SucursalViewSet, DireccionesViewSet, ClienteViewSet, TarjetaViewSet

router = routers.SimpleRouter()
router.register(r'prestamos', PrestamoViewSet, basename='prestamos')
router.register(r'cuentas', CuentasViewSet, basename='cuentas')
router.register(r'direcciones', DireccionesViewSet, basename='direcciones')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'tarjetas', TarjetaViewSet, basename='tarjetas')

urlpatterns = [
    path('sucursales/',
         SucursalViewSet.as_view({'get': 'list'}), name='sucursales'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
