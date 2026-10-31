from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfesionalViewSet, CitaMedicaViewSet

router = DefaultRouter()
router.register(r'profesionales', ProfesionalViewSet)
router.register(r'citas', CitaMedicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]