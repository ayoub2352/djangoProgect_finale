from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Categorie)
admin.site.register(Client)
admin.site.register(Voyage)
admin.site.register(Client_voyage)
admin.site.register(Adminstrateur)
admin.site.register(Vol)
admin.site.register(Hotel)