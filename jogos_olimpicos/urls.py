from rest_framework.routers import DefaultRouter
from jogos_olimpicos import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'atleta', views.AtletaViewSet)
router.register(r'competicao', views.CompeticaoViewSet)
router.register(r'resultado', views.ResultadoViewSet)