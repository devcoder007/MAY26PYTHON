from django.urls import path
from . import views


urlpatterns = [
    path('crud/', views.UserApisView.as_view()),
    path('crud/<int:pk>', views.UserApisView.as_view()),
]
