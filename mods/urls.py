from django.urls import path
from . import views

urlpatterns = [
    path('', views.models_hp, name='Model Market Home Page'),
    path("/<int:model_id>", views.model_details, name='Model Details')
]