from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'

    name = models.CharField(max_length=50)
  
    def __str__(self):
            return f'{self.name} '

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Nome")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="Sobre Nome")
    phone = models.CharField(max_length=50, verbose_name="Telefone")
    email = models.EmailField(max_length=254, blank=True, verbose_name="E-Mail")
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default =True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, 
        verbose_name=("categorias"),
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
       

    def __str__(self):
        return f'{self.first_name} { self.last_name}'
    