from django.urls import path

from .views import index, by_rubric, BbCreateView

# ZHE сылки в прямом виде
# urlpatterns = [
#     path('<int:rubric_id>/', by_rubric),
#     path('', index),
# ]

# ZHE именованные маршруты
urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]