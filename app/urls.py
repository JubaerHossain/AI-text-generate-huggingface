from django.urls import path
from . import views

urlpatterns = [
    path('text', views.prompt_data, name='prompt_data'),
]
