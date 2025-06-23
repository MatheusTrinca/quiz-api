import graphene
from graphene_django import DjangoListField, DjangoObjectType

from .models import Answer, Category, Question, Quizz


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzType(DjangoObjectType):
    class Meta:
        model = Quizz
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query(graphene.ObjectType):
    all_questions = DjangoListField(QuestionType, id=graphene.Int())
    all_answers = DjangoListField(AnswerType, id=graphene.Int())

    def resolve_all_questions(self, info, **kwargs):
        if kwargs.get("id", None) is None:
            return Question.objects.all()
        return Question.objects.filter(pk=kwargs.get("id", None))

    def resolve_all_answers(self, info, **kwargs):
        if kwargs.get("id", None) is None:
            return Answer.objects.all()
        return Answer.objects.filter(question=kwargs.get("id", None))


schema = graphene.Schema(query=Query)
