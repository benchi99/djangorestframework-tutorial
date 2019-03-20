from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    """    
    Permiso personalizado para que solo los autores de un objeto puedan editarlo.
    """

    def has_object_permission(self, request, view, obj):
        # Los permisos de lectura están disponibles para
        # todos, asi que los métodos GET, HEAD y OPTIONS
        # estarán disponibles para todo el mundo.

        if request.method in permissions.SAFE_METHODS:
            return True

        # Los permisos de escritura solo están disponibles
        # para el autor del snippet.

        return obj.autor == request.user