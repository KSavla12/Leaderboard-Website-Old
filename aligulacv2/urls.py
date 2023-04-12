from django.urls import path
# from .views import line_chart, line_chart_json
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('player_list/', views.player_list, name='player_list'), 
    path('player_page/<str:player>', views.player_page, name='player_page'),
    path('search/', views.search, name='search'), 
]

urlpatterns += staticfiles_urlpatterns()