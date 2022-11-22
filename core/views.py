from rest_framework import viewsets
from rest_framework import viewsets
# REQUIRED TOKEN AUTHENTICATION
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.db import connection

from .models.db_crm import (
    TbOrganizacao, 
    TbUsuario,
    TbGrupo,
    TbGrupoUsuario,
    TbRelatorio
)
from .serializer.crm import (
    OrganizacaoSerializer, 
    UsuarioSerializer,
    GrupoSerializer,
    GrupoUsuarioSerializer,
    RelatorioSerializer
)

cursor = connection.cursor()

class OrganizacaoViewSet(viewsets.ModelViewSet):
    queryset = TbOrganizacao.objects.all()
    serializer_class = OrganizacaoSerializer
    permission_classes = [AllowAny] 
    http_method_names = ['get', 'post']

   
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = TbUsuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = TbGrupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated]

class GrupoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TbGrupoUsuario.objects.all()
    serializer_class = GrupoUsuarioSerializer
    permission_classes = [IsAuthenticated]

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = TbRelatorio.objects.all()
    serializer_class = RelatorioSerializer
    permission_classes = [IsAuthenticated]


class LoginViewSet(viewsets.ModelViewSet):
    queryset = TbUsuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get']

    def get_queryset(self):
        queryset = TbUsuario.objects.all()
        username = self.request.query_params.get('username', None)
        password = self.request.query_params.get('password', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        if password is not None:
            queryset = queryset.filter(password=password)
        return queryset



    