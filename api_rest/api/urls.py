from django.urls import path, include
from portfolios.views import PortfolioListView

urlpatterns = [
    path('portfolios/',PortfolioListView.as_view(), name='portfolios'),
]
