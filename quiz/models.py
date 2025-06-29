from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Quizz(models.Model):
    title = models.CharField(max_length=255, default=_("New Quiz"))
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Quizz")
        verbose_name_plural = _("Quizzes")

    def __str__(self):
        return self.title


class Question(models.Model):
    SCALE = (
        (0, _("Fundamental")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert")),
    )

    TYPE = ((0, _("Multiple Choice")),)

    quiz = models.ForeignKey(
        Quizz, related_name="question", on_delete=models.DO_NOTHING
    )
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question")
    )
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_("Difficulty")
    )
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created")
    )
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="answer", on_delete=models.DO_NOTHING
    )
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
