#coding: utf-8
from rest_framework import serializers
from .models import DadosPessoais

class DadosPessoaisSerializer(serializers.MoldelSerializer):

    class Meta:
        model = DadosPessoais
        depth = 1
        fields =['id','name', 'adress', 'city', 'cep', 'phone', 'mobile']
