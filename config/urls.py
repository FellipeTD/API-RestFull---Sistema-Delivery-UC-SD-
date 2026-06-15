"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from delivery.views import userViewSet,produtoViewSet, estabelecimentoViewSet,listaViewSet,pedidoViewSet,enderecoViewSet, listaUser, listaEstabelecimento, listaProduto, listaPedido, listaEndereco
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register('users', userViewSet, basename='users')
router.register('estabelecimentos', estabelecimentoViewSet, basename='estabelecimentos')
router.register('listas',listaViewSet,basename='listas')
router.register('produtos',produtoViewSet,basename='produtos')
router.register('pedidos',pedidoViewSet,basename='pedidos')
router.register('enderecos',enderecoViewSet,basename='enderecos')

schema_view = get_schema_view(
    openapi.Info(
        title="API Delivery",
        default_version='v1',
        description="Documentação da API de Delivery",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('users/<int:pk>/listas/',listaUser.as_view()),
    path('estabelecimentos/<int:pk>/listas/',listaEstabelecimento.as_view()),
    path('produtos/<int:pk>/listas/',listaProduto.as_view()),
    path('pedidos/<int:pk>/listas/',listaPedido.as_view()),
    path('enderecos/<int:pk>/listas/',listaEndereco.as_view()),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger'),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
]