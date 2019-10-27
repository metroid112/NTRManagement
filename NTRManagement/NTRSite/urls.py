from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.design_list, name='design_list'),
    path('<int:design_id>/', views.design_detail, name='design_detail')
]