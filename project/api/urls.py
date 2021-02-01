from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
        SurveyViewSet, QuestionViewSet, ActiveSurveysListView,
        AnswerToTheQuestionView, ShowSurveysUserView
    )


router = DefaultRouter()
router.register(r'administrator/surveys', SurveyViewSet, basename='survey')
router.register(r'administrator/questions', QuestionViewSet,
                basename='question')
router.register(r'answers', AnswerToTheQuestionView, basename='answer')


urlpatterns = [
    path(r'list-active-surveys/', ActiveSurveysListView.as_view()),
    path(r'answered-surveys/', ShowSurveysUserView.as_view())
] + router.urls
