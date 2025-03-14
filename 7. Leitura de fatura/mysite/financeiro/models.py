from django.db import models
from djmoney.models.fields import MoneyField
import datetime
import django
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
description_length = 30
# Create your models here.
class BankAccount(models.Model):
   balance = MoneyField(default=0,max_digits=14, decimal_places=2, default_currency='BRL')
   #balance.default = 0
   #def __str__ (self):
      #return self.balance
class Movement(models.Model):
   STATUS=[
      ('pago_cred_nu','Pago Crédito Nubank'),
      ('pago_cred_bb', 'Pago Crédito Banco do Brasil'),
      ('pago_cred_it', 'Pago Crédito Itaú'),
      ('pago_pix', 'Pago Pix'),
      ('a_pagar','A Pagar'),
      ('prev','Previsionado')]
   TIPOS=[
      ('ass','Assinatura'),
      ('fat_nu','Fatura Nubank'),
      ('fat_bb','Fatura Banco do Brasil'),
      ('fat_it','Fatura Itaú'),
      ('AC_&_blz','Autocuidado e Beleza'),
      ('','')
      ]
   categoria = models.CharField(max_length=30,choices=STATUS)
   value = MoneyField(default=0,max_digits=14, decimal_places=2, default_currency='BRL')
   date = models.DateField(default=django.utils.timezone.now)
   description = models.CharField(default='',max_length=description_length)
   def __str__ (self):
      return str(self.date.strftime('%a %d/%m/%Y').capitalize())+': '+self.description +' - '+str(self.value)
   class Meta:
     abstract = True

class Entry(Movement):
   class Meta(Movement.Meta):
      db_table = 'Entradas'
class Exit(Movement):
   class Meta(Movement.Meta):
      db_table = 'Saídas'
   
