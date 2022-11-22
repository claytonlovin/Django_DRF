# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class TbGrupo(models.Model):
    id_grupo = models.AutoField(db_column='ID_GRUPO', primary_key=True)  # Field name made lowercase.
    nome_do_grupo = models.CharField(db_column='NOME_DO_GRUPO', max_length=20)  # Field name made lowercase.
    data_criacao = models.DateTimeField(db_column='DATA_CRIACAO', blank=True, null=True)  # Field name made lowercase.
    fl_ativo = models.IntegerField(db_column='FL_ATIVO', blank=True, null=True)  # Field name made lowercase.
    id_organizacao = models.ForeignKey('TbOrganizacao', models.DO_NOTHING, db_column='ID_ORGANIZACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_grupo'


class TbGrupoUsuario(models.Model):
    id_grupo_usuario = models.AutoField(db_column='ID_GRUPO_USUARIO', primary_key=True)  # Field name made lowercase.
    id_grupo = models.ForeignKey(TbGrupo, models.DO_NOTHING, db_column='ID_GRUPO')  # Field name made lowercase.
    id_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='ID_USUARIO')  # Field name made lowercase.
    id_organizacao = models.ForeignKey('TbOrganizacao', models.DO_NOTHING, db_column='ID_ORGANIZACAO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_grupo_usuario'

class TbOrganizacao(models.Model):
    id_organizacao = models.AutoField(db_column='ID_ORGANIZACAO', primary_key=True)  # Field name made lowercase.
    nome_organizacao = models.CharField(db_column='NOME_ORGANIZACAO', max_length=100)  # Field name made lowercase.
    data_criacao = models.DateField(db_column='DATA_CRIACAO')  # Field name made lowercase.
    fl_ativo = models.IntegerField(db_column='FL_ATIVO')  # Field name made lowercase.
    user_empresa = models.CharField(db_column='USER_EMPRESA', unique=True, max_length=250, blank=True, null=True)  # Field name made lowercase.
    senha_empresa = models.CharField(db_column='SENHA_EMPRESA', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_organizacao'


class TbRelatorio(models.Model):
    id_relatorio = models.AutoField(db_column='ID_RELATORIO', primary_key=True)  # Field name made lowercase.
    ds_nome_relatorio = models.CharField(db_column='DS_NOME_RELATORIO', max_length=100)  # Field name made lowercase.
    ds_link_relatorio = models.CharField(db_column='DS_LINK_RELATORIO', max_length=1024)  # Field name made lowercase.
    id_grupo = models.ForeignKey(TbGrupo, models.DO_NOTHING, db_column='ID_GRUPO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_relatorio'


class TbUsuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_USUARIO', primary_key=True)  # Field name made lowercase.
    nome_usuario = models.CharField(db_column='NOME_USUARIO', unique=True, max_length=100)  # Field name made lowercase.
    ds_telefone = models.CharField(db_column='DS_TELEFONE', unique=True, max_length=15)  # Field name made lowercase.
    ds_email = models.CharField(db_column='DS_EMAIL', unique=True, max_length=100)  # Field name made lowercase.
    ds_login = models.CharField(db_column='DS_LOGIN', unique=True, max_length=30)  # Field name made lowercase.
    ds_senha = models.CharField(db_column='DS_SENHA', unique=True, max_length=30)  # Field name made lowercase.
    fl_administrador = models.IntegerField(db_column='FL_ADMINISTRADOR', blank=True, null=True)  # Field name made lowercase.
    id_organizacao = models.ForeignKey(TbOrganizacao, models.DO_NOTHING, db_column='ID_ORGANIZACAO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_usuario'
