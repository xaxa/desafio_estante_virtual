from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('jogos_olimpicos.urls')),
]