from rest_framework.routers import DefaultRouter
from core import views


router = DefaultRouter()
router.register(r'organizacao', views.OrganizacaoViewSet, basename='organizacao',)
router.register(r'usuario', views.UsuarioViewSet, basename='usuario',)
router.register(r'grupo', views.GrupoViewSet, basename='grupo',)
router.register(r'grupousuario', views.GrupoUsuarioViewSet, basename='grupousuario',)
router.register(r'relatorio', views.RelatorioViewSet, basename='relatorio',)
router.register(r'login', views.LoginViewSet, basename='login',)

