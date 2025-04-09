from rest_framework import viewsets
from .model import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewwsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer