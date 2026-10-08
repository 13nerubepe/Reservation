"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets  # noqa: F401  (a utiliser)

from .models import Reservation, Salle  # noqa: F401  (a utiliser)

# TODO : votre code ici

Class SalleViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve", "occupation"]:
            permission_classes = [AllowAny]
        else :
            permission_classes = [IsAdminUser]
        return [get_permission() for permission in permission_classes]

    @action(detail=True, methode= ["get"], url_path="occupation")
    def occupation(self, request, pk=None):


Class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
            if self.action in ["list", "retrieve"]:
                permission_classes = [AllowAny]
            elif self.action == "create"
                permission_classes = [IsAuthentificated]
            else :
                permission_classes = [IsAuthentificated, IsOwnerOrReadOnly]
            return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(utilisateur = self.request.user)
