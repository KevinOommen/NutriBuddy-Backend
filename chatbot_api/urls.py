from django.urls import path
from .views import ChatBotView_FoodSearch,ChatBotView_DietSelector

urlpatterns = [
    path("food_search/",ChatBotView_FoodSearch.as_view(),name="food_search"),
    path("diet_selector/",ChatBotView_DietSelector.as_view(),name="diet_selector"),
]


