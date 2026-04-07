from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Permission, Role, User
from .serializers import PermissionSerializer, RoleSerializer, UserSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def check_permission(request, user_id, permission_name):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(
            {"error": "User not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if user.role is None:
        return Response(
            {"user": user.username, "permission": permission_name, "has_access": False}
        )

    has_permission = user.role.permissions.filter(name=permission_name).exists()

    return Response({
        "user": user.username,
        "role": user.role.name,
        "permission": permission_name,
        "has_access": has_permission
    })