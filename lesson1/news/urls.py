from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewSingleNews.as_view(), name='view_single_news'),
    path('news/add-news/', CreateNews.as_view(), name="add_news"),
]