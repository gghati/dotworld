from restapp.views import *
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('certificate/', Certificate.as_view(), name='certificate'),
    path('workexp/', WorkExp.as_view(), name='workexp'),
    path('projects/', Projects.as_view(), name='project')
]
