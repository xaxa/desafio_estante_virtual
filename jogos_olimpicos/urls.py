from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from jogos_olimpicos import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'atleta', views.AtletaViewSet)
router.register(r'competicao', views.CompeticaoViewSet)
router.register(r'resultado', views.ResultadoViewSet)

finalizar_competicao = views.CompeticaoViewSet.as_view({
    'get': 'finalizarCompeticao'
})

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^competicao/(?P<pk>[0-9]+)/finalizar/$',finalizar_competicao,name='finalizar-competicao')
]