#!/usr/bin/env python
# coding: utf-8

# ## Lista convidados

# In[1]:


# Criamos 3 listas vazias para receber o nome dos convidados da lista
# A idade de cada um
# E a lista nome_lista serve para verificar se o nome inserido pelo usuario coincide com algum nome armazenado na lista nome.
nome = []
idade = []
nome_lista = []
# Pedimos a quantidade de convidados da lista para limitar o nosso laço for
qtd_convidados = int(input("Número de convidados: "))

# Pegando os nomes dos convidados para colocar na lista
for i in range(qtd_convidados):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    # Verificando se a idade é menor que 18 anos, pois se for, entrada proibida!!!
    if idade < 18:
        print("Desculpe, você não está autorizado a entrar!")
        
print("-"*4, "LISTA DE CONVIDADOS", "-"*4)

# Aqui é o laço em que verificamos se o nome do usuário consta na lista!
for j in range(3):
    nomeLista = input("Nome: ")
    if nomeLista != nome:
        print("Desculpe, mas você não está na lista de convidados!")
    else:
        print("Seja bem-vindo(a). Aproveite!")


# In[ ]:




