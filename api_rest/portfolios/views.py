from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import DadosPessoais
from .serializer import DadosPessoaisSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

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

    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "403 Forbidden"},
                            status=status.HTTP_409_CONFLICT)

class PortfolioView(APIView):
    def get(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        DadosPessoais.delete(user)
        return Response({"message": "Usuario deletado"},
                            status = status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user=DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status = status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"404 error"},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
