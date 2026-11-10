from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Vazifa nomi")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")
    is_completed = models.BooleanField(default=False, verbose_name="Bajarildi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vazifa"
        verbose_name_plural = "Vazifalar"