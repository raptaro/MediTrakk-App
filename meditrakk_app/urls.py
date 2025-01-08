from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('appointments.urls')),
    path('', include('user.urls')),
    path('', include('core.urls', namespace='core')),
    path('', include('patient.urls', namespace='patient')),
    path('', include('queueing.urls', namespace='queueing'))


]

