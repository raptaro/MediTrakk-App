from django.urls import path
from . import views

app_name = 'core' # Add this line

urlpatterns = [
    path('', views.dashboard, name='home'),

]