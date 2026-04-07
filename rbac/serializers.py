from rest_framework import serializers
from .models import Permission, Role, User

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    permission_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Permission.objects.all(),
        source='permissions', write_only=True
    )

    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions', 'permission_ids']


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        source='role', write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'role_id']