"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers

from .models import Reservation, Salle  # noqa: F401  (a utiliser)

# TODO : votre code ici

Class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(utilisateur =self.request.user)


Class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields =["nom", "capacite", "batiment"]


Class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
            model = Reservation
            fields =["salle", "utilisateur", "salle", "debut",
             "fin", "motif", "utilisateur", "statut","cree_le"]
#             cest en lecture seule
            read_only_fields =["id", "utilisateur", "cree_le"]

    def valite_reservation(self,value):
#         creation
        if self.instance is None:
            salle = value.get("salle")
