from rest_framework import generics
from .models import ToDo
from .seializers import todoSerializer

class ToDoGetCreate(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = todoSerializer

class ToDoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = todoSerializer
    lookup_field = ['title', 'desc']

