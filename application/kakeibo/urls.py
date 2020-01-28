from django.urls import path
from . import views

app_name = "kakeibo"

urlpatterns = [
    path('', views.KakeiboListView.as_view(), name="kakeibo_list"),

    path('kakeibo_create/', views.KakeiboCreateView.as_view(), name="kakeibo_create"),
    path('kakeibo_update/<int:pk>', views.KakeiboUpdateView.as_view(), name="kakeibo_update"),
    path('kakeibo_delete/<int:pk>', views.KakeiboDeleteView.as_view(), name="kakeibo_delete"),

    path('category_list/', views.CategoryListView.as_view(), name="category_list"),
    path('category_create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category_update/<int:pk>', views.CategoryUpdateView.as_view(), name="category_update"),
    path('category_delete/<int:pk>', views.CategoryDeleteView.as_view(), name="category_delete"),

    path('create_done/', views.create_done, name="create_done"),
    path('update_done/', views.update_done, name="update_done"),
    path('delete_done/', views.delete_done, name="delete_done"),

    path('circle_chart/', views.show_circle_chart, name="circle_chart"),
    path('linear_chart/', views.show_linear_chart, name="linear_chart"),
]
