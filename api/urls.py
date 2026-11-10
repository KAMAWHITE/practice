from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health_check, TaskViewSet, RegisterView

# Router avtomatik ravishda barcha URL'larni generatsiya qiladi
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),  # /api/v1/tasks/ va /api/v1/tasks/{id}/ avtomatik ulanadi
]
