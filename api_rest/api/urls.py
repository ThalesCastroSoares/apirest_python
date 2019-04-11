from django.urls import path, include
from portfolios.views import PortfolioView, PortfolioListView


urlpatterns = [
    path('portfolios/',PortfolioListView.as_view(), name='portfolios'),
    #Nao se utiliza mais a expressao regular
    #(?P<pk>[0-9]+) se tornou <int:pk>...
    path('portfolios/<int:pk>/',PortfolioView.as_view(), name='get_portfolio'),
]
