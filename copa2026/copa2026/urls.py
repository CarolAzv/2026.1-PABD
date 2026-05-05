from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from torneio import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'grupos', views.GrupoViewSet, basename='grupos')
router.register(r'tecnicos', views.TecnicoViewSet, basename='tecnicos')
router.register(r'selecoes', views.SelecaoViewSet, basename='selecoes')
router.register(r'jogadores', views.JogadorViewSet, basename='jogadores')
router.register(r'jogos', views.JogoViewSet, basename='jogos')
router.register(r'eventos', views.EventoJogoViewSet, basename='eventos-jogo')

schema_view = get_schema_view(
    openapi.Info(
        title="API Copa 2026",
        default_version='v1',
        description="API RESTful para o gerenciamento da Copa do Mundo de 2026",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("copa_api/", include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
