from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1 import school, classroom, teacher, student

router = DefaultRouter()

router.register(r'schools', school.SchoolViewSet, basename='school')
router.register(r'classrooms', classroom.ClassroomViewSet, basename='classroom')
router.register(r'teachers', teacher.TeacherViewSet, basename='teacher')
router.register(r'students', student.StudentViewSet, basename='student')

print("Registered Routes:")
for route in router.urls:
    print(route)

urlpatterns = [
    path('v1/', include(router.urls)),
]
