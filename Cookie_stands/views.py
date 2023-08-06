from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookie_stand
from .permissions import IsOwnerOrReadOnly
from .serializers import Cookie_standSerializer


class Cookie_standList(ListCreateAPIView):
    queryset = Cookie_stand.objects.all()
    serializer_class = Cookie_standSerializer


class Cookie_standDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly)
    queryset = Cookie_stand.objects.all()
    serializer_class = Cookie_standSerializer
