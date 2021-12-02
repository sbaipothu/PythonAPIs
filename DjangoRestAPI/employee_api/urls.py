from django.urls import path, include
from .views import EmployeeViewSet, CourseViewSet, PersonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee_details', EmployeeViewSet, basename='employee')
router.register('course_details', CourseViewSet, basename='course')
router.register('person_details', PersonViewSet, basename='person')

urlpatterns =[
    path('employee_api/', include(router.urls))
]
