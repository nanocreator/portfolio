from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
    path('contact/', views.contact, name='contact'),
]