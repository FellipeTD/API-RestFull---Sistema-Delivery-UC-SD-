from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import user, estabelecimento, lista

class users(admin.ModelAdmin):
    list_display = ('id','nome','email','cpf','data_nascimento','celular')
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(user,users)

# código omitido

class estabelecimentos(admin.ModelAdmin):
    list_display = ('id','codigo','descricao')
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)
admin.site.register(estabelecimento,estabelecimentos)

class listas(admin.ModelAdmin):
    list_display = ('id','user','estabelecimento')
    list_display_links = ('id',)
admin.site.register(lista,listas)
