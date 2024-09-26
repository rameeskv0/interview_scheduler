# urls.py (scheduler app)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'availabilities', views.AvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('candidate/<int:candidate_id>/availability/', views.input_candidate_availability, name='input_candidate_availability'),
    path('interviewer/<int:interviewer_id>/availability/', views.input_interviewer_availability, name='input_interviewer_availability'),
    path('user/<int:user_id>/availability/', views.get_user_availability, name='get_user_availability'),
    path('get_available_slots/', views.get_available_slots, name='get_available_slots'),
]
