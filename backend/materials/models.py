from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    preview = models.ImageField(
        upload_to="courses/preview", verbose_name="превью курса", null=True, blank=True
    )
    description = models.TextField(verbose_name="описание", null=True, blank=True)

    def __str__(self):
        return f"Course: {self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="курс", related_name="lessons"
    )
    name = models.CharField(max_length=255, verbose_name="название")
    preview = models.ImageField(
        upload_to="lessons/preview", verbose_name="превью урока", null=True, blank=True
    )
    description = models.TextField(
        verbose_name="описание",
    )
    video = models.FileField(
        upload_to="lessons/video", verbose_name="Видео к уроку", null=True, blank=True
    )

    def __str__(self):
        return f"Lesson: {self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
