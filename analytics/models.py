from django.db import models


class Visit(models.Model):
    page = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(blank=True)
    referrer = models.URLField(max_length=500, blank=True)
    ip_anonimizada = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.page} — {self.timestamp:%Y-%m-%d %H:%M}'
