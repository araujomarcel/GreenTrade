from django.db import models


class ClienteModel(models.Model):
    cpf = models.CharField('cpf', max_length=11, unique=True)
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=50)
    email = models.CharField('email', max_length=30)
    user_type = models.CharField('user_type', max_length=10, default='cliente')
    password = models.CharField('senha', max_length=15)
    pontuacao = models.IntegerField(default=0)


class EmpresaModel(models.Model):
    cnpj = models.CharField('cnpj',max_length=14)
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=50)
    email = models.CharField('email', max_length=30)
    password = models.CharField('senha', max_length=15)
    
class LoginModel(models.Model):
    cpf = models.CharField('cpf', max_length=11)
    password = models.CharField('password', max_length=15)

class ProdutoModel(models.Model):
    metais = models.CharField('metais', max_length=14)
    eletronicos = models.CharField('eletronicos', max_length=14)
    plastico = models.CharField('plastico', max_length=14)
    quantidade = models.CharField('quantidade', max_length=14)

class TrocasForm(models.Model):
    produto_macarrao= models.CharField('produto_macarrao',max_length=14)
    produto_frango= models.CharField('produto_frango',max_length=14)
    produto_leite= models.CharField('produto_leite',max_length=14)
    produto_requeijao= models.CharField('produto_requeijao',max_length=14)
    quantidade = models.CharField('quantidade', max_length=14)