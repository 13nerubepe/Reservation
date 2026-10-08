"""Tache 4 : permissions personnalisees.

A FAIRE :
  - IsOwnerOrReadOnly : lecture pour tous, modification/suppression
    reservee a l'auteur de la reservation (obj.utilisateur).
"""
from rest_framework import permissions  # noqa: F401  (a utiliser)
from rest_framework.permissions import BasePermission, SAFE_METHODS

# TODO : votre code ici
class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
#         get, head, options
        if request.method in permissions.SAFE_METHODS:
            return True
#             put, patch, delete
        return obj.utilisateur == request.user

