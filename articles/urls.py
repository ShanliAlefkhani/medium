from django.urls import path
from articles import views


urlpatterns = [
	path('', views.ArticleList.as_view()),
]

