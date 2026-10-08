"""Routes racine du projet."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Connexion/deconnexion pour la Browsable API de DRF
    path("api-auth/", include("rest_framework.urls")),
    # Routes de l'API (a completer dans salles/urls.py)
    path("api/", include("salles.urls")),

    path("api/salles/", include("salles.urls")),
    path("api/salles/{id}", include("salles.urls")),
    path("api/reservations/", include("reservations.urls")),
    path("api/reservations/{id}", include("reservations.urls")),
    path("api/salles/{id}/occupation/", include("reservations.urls")),
]
