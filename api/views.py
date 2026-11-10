from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .serializers import TaskSerializer, RegisterSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def health_check(request):
    return Response({
        "status": "success",
        "message": "Django REST API muvaffaqiyatli ishlayapti, Boss!",
        "version": "1.0.0"
    })

class TaskViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet barcha CRUD (Create, List, Retrieve, Update, Destroy)
    amallarini avtomatik bajarib beradi!
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_completed']

class RegisterView(generics.CreateAPIView):
    """
    Yangi foydalanuvchini ro'yxatdan o'tkazish uchun API endpoint
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]