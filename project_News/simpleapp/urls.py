from django.urls import path
from .views import NewDetail, NewsList # импортируем наше представление

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewDetail.as_view()),
]