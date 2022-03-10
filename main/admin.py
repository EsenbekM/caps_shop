from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Size)
admin.site.register(models.Brand)
admin.site.register(models.Cap)
admin.site.register(models.Bestsaller)
admin.site.register(models.Event)


