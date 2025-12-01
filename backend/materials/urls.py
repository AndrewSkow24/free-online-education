from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from .apps import MaterialsConfig

app_name = MaterialsConfig.name


router = SimpleRouter()

router.register("", views.CourseViewSet, basename="courses")

urlpatterns = [
    path(
        "lessons/", views.LessonListCreateAPIView.as_view(), name="lesson_list_create"
    ),
    path(
        "lessons/<int:pk>/",
        views.RetrieveUpdateDestroyAPIView.as_view(),
        name="lesson_retrieve_update_destroy",
    ),
] + router.urls
