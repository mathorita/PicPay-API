from django.db import models

#Nome Completo, CPF, e-mail e Senha
class User(models.Model):
    USER_TYPE = (
        ('L','Lojista'),
        ('C','Cliente'),
    )
    nome_completo = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100, unique=True)
    user_type = models.CharField(max_length=1,choices=USER_TYPE,blank=False,null=False,default='C')
    wallet = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.nome_completo

class Transaction(models.Model):
    sender = models.ForeignKey('User', related_name='sent_money',on_delete=models.CASCADE)
    receiver = models.ForeignKey('User', related_name='received_money', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender.nome_completo} → {self.receiver.nome_completo} | R$ {self.value}"
    