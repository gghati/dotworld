from restapp.views import *
from django.urls import path

urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', Simple.as_view(), name='simple'),
    path('certificate/', Certificate.as_view(), name='certificate'),
    path('workedfor/', WorkedFor.as_view(), name='workfor'),
    path('projects/', Projects.as_view(), name='project'),
    path('blogs/', Blogs.as_view(), name='blogs'), 
    path('opensource/', OpenSource.as_view(), name='opensource'),
    path('ridingsolo/', RidingSolo.as_view(), name='ridingsolo'),
    path('gist/<slug:pagename>/', GistPages.as_view(), name='gistpages')
]
