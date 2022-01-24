from django.urls import path
from . import views
from .views import CreateComa

app_name = 'editlecture'

urlpatterns = [
    path('create_coma/',CreateComa.as_view(),name='create_coma')
]