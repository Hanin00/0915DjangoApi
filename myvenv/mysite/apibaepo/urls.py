from django.urls import path, include
from . import views


app_name = 'lift'
urlpatterns = [
    path('list/', views.lift_view, name = 'index'),
    path('total/', views.lift_list),
    path('liftdetail/<int:pk>/', views.lift_detail),
]
