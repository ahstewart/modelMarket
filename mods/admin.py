from django.contrib import admin
from .models import NNmodel

# make models available to admin site
admin.site.register(NNmodel)
