from rest_framework import serializers
from core.models.db_crm import (
    TbOrganizacao, 
    TbUsuario,
    TbGrupo,
    TbGrupoUsuario,
    TbRelatorio
)


    
class OrganizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbOrganizacao
        fields = ['id_organizacao', 'nome_organizacao', 'data_criacao', 'fl_ativo']
    
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbUsuario
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbUsuario
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbGrupo
        fields = '__all__'

class GrupoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbGrupoUsuario
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbRelatorio
        fields = '__all__'