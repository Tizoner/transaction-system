from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import generics, status

from .models import Client, Transaction
from .serializers import ClientSerializer, TransactionSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


@extend_schema_view(
    get=extend_schema(
        summary="получение списка транзакций, инициированных пользователем",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                TransactionSerializer,
                description="Запрос успешно выполнен",
            )
        },
    )
)
class ClientTransactionsList(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(client__id=self.kwargs["pk"])
