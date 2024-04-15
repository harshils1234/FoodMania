from django.urls import path
from foodmania.views import CategoryCreateView, CategoryListView, CategoryUpdateView, \
    CategoryDeleteView, FoodCreateView, FoodListView, FoodUpdateView, FoodDeleteView

app_name = 'foodmania'

urlpatterns = [


    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('food/create/', FoodCreateView.as_view(), name='food_create'),
    path('food/list/', FoodListView.as_view(), name='food_list'),
    path('food/update/<str:pk>/', FoodUpdateView.as_view(), name='food_update'),
    path('food/delete/<str:pk>/', FoodDeleteView.as_view(), name='food_delete')


]
