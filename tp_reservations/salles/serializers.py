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

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ["nom", "capacite", "batiment"]


class ReservationSerializer(serializers.ModelSerializer):
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

#     pas compris
    def validate(self, data):

            debut = data.get("debut")
            fin = data.get("fin")
            salle = data.get("salle")

            if debut and fin and fin <= debut:
                raise serializers.ValidationError({
                    "fin": "La fin doit être strictement après le début."
                })

            if salle and debut and fin:

                reservations = Reservation.objects.filter(
                    salle=salle,
                    statut="CONFIRMEE",
                    debut__lt=fin,
                    fin__gt=debut,
                )

                # Lors d'une modification, on exclut la réservation
                # actuellement modifiée.
                if self.instance is not None:
                    reservations = reservations.exclude(
                        pk=self.instance.pk
                    )

                if reservations.exists():
                    raise serializers.ValidationError({
                        "non_field_errors": [
                            "La salle est déjà réservée sur cette période."
                        ]
                    })
