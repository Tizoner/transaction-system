from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import (
    ClientDetail,
    ClientList,
    ClientTransactionsList,
    TransactionDetail,
    TransactionList,
)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view()),
    path(
        "clients/",
        include(
            [
                path("", ClientList.as_view()),
                path(
                    "<int:pk>/",
                    include(
                        [
                            path("", ClientDetail.as_view()),
                            path("transactions/", ClientTransactionsList.as_view()),
                        ]
                    ),
                ),
            ]
        ),
    ),
    path(
        "transactions/",
        include(
            [
                path("", TransactionList.as_view()),
                path("<int:pk>", TransactionDetail.as_view()),
            ]
        ),
    ),
]
