from django.urls import path
from .views import ChatBotView_FoodSearch

urlpatterns = [
    path("food_search/",ChatBotView_FoodSearch.as_view(),name="food_search"),
]


