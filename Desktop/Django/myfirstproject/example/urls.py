from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('iletisim', views.iletisim),
    path('hakkimizda', views.hakkimizda),
    path('example', views.example),
    path('<kurs_adi>', views.details),                                                                      #dinamik url
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),                                       #dinamik url
    path('kategori/<str:category_name>', views.getCoursesByCategory, name = 'courses_by_category'),         #dinamik url
    
]
