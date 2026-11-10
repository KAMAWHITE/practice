from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'created_at')  # Admin jadvalida ko'rinadigan ustunlar
    list_filter = ('is_completed', 'created_at')                  # Filtrlash uchun panellar
    search_fields = ('title', 'description')                      # Qidiruv maydonlari