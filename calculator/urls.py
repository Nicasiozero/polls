from django.urls import path
from . import views

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     re_path(r'^example/(?P<value>[1-5]{4})/$', views.example_view),
#     # path('calculate/', views.calculate, name='calculate'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^example/(?P<value>[1-5]{4})/$', views.example_view),
    # path('calculate/', views.calculate, name='calculate'),
]
