from rest_framework.generics import ListAPIView, CreateAPIView

from billing.api.serializers import UserSerializer, InvoiceSerializer
from users.models import User


class ClientList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class InvoiceCreate(CreateAPIView):
    serializer_class = InvoiceSerializer
