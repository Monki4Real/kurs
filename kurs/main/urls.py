from django.urls import path
from django.contrib import admin
from . import views
from .views import news_detail, news_list
from .views import custom_admin_dashboard
from .views import login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about),
    path('news/', news_list, name='news_list'),
    path('rules', views.rules),
    path('', views.cheatsheet, name="cheatsheet"),
    path('download/<int:cheatsheet_id>/',
         views.download_cheatsheet, name='download_cheatsheet'),
    path("robots.txt", views.robots_txt),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('custom_admin/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('custom_admin/news/', views.manage_news, name='manage_news'),
    path('custom_admin/news/add/', views.add_or_edit_news, name='add_news'),
    path('custom_admin/news/edit/<int:news_id>/', views.add_or_edit_news, name='edit_news'),
    path('custom_admin/news/delete/<int:news_id>/', views.delete_news, name='delete_news'),
    path('custom_admin/cheatsheets/', views.manage_cheatsheets, name='manage_cheatsheets'),
    path('custom_admin/cheatsheets/add/', views.add_or_edit_cheatsheet, name='add_cheatsheet'),
    path('custom_admin/cheatsheets/edit/<int:cheatsheet_id>/', views.add_or_edit_cheatsheet, name='edit_cheatsheet'),
    path('custom_admin/cheatsheets/delete/<int:cheatsheet_id>/', views.delete_cheatsheet, name='delete_cheatsheet'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]








    




