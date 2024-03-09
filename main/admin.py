from django.contrib import admin

from . import models


admin.site.register(models.Place)
admin.site.register(models.Category)
admin.site.register(models.MenuItem)
admin.site.register(models.Order)
admin.site.register(models.Tag)
admin.site.register(models.UserSession)
admin.site.register(models.Invoice)
admin.site.register(models.OrderItem)
admin.site.register(models.UserProfile)
admin.site.register(models.UserTagCount)