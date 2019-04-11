from django.shortcuts import render

from .models import DadosPessoais
from .serializer import DadosPessoaisSerializer

from rest_framework.response import Response
from rest_framework.viwews import APIView

# Create your views here.
def exibir_portfolio(request):
    pessoa = DadosPessoais.objects.all()
    context = {'pessoa':pessoa}
    return render(request, 'portfolios/exibir_portfolio.html', context)

class PortfolioListView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)
