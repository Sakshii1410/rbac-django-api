from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PermissionViewSet, RoleViewSet, UserViewSet, check_permission

router = DefaultRouter()
router.register(r'permissions', PermissionViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('check-permission/<int:user_id>/<str:permission_name>/', check_permission),
]