from django.urls import path
from .views import ListeProjetsView, DetailProjetView
app_name = 'project'

urlpatterns = [
    path('', ListeProjetsView.as_view(), name='projects'),
    path('<int:pk>/', DetailProjetView.as_view(), name='project_detail'),
]
