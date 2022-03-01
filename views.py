from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
from .models import News
from datetime import datetime
from .filters import NewsFilter



class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        return context



class NewDetail(DetailView):
    model = News  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html'  # название шаблона будет new.html
    context_object_name = 'news'  # название объекта. в нём будет

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        return context



class News_s(ListView):

    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_s'
    ordering = ['-id']
    paginate_by = 1 # поставим постраничный вывод в один элемент

    def get_context_data(self,**kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context