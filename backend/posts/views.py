from rest_framework import generics

from .models import View
from .serializers import ViewSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = View.objects.all()
    serializer_class = ViewSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = View.objects.all()
    serializer_class = ViewSerializer