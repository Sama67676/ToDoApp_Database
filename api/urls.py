from .views import ToDoGetCreate, ToDoUpdateDelete
from django.urls import path, include


urlpatterns = [
    path('<int:pk>', ToDoUpdateDelete.as_view()),
    path('', ToDoGetCreate.as_view())
]
