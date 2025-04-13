from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectList.as_view(), name='portfolio'),
    path('projects/<slug:slug>/', ProjectDetail.as_view(), name='project_detail'),
    # path('contact/', ContactView.as_view(), name='contact'),
]
