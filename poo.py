# Programação Orientada a objetos (POO) / object ooriented programing (OOP)
# um classe tem atributos e metodos (funçoes)

class Cliente:
def _init_(self, nome): # construtor
    self.nome = nome
    self.pontuacao  = 5
    self.premium = false
def aumenta_pontuacao(self):
   if self.pontuacao == 5:
    self.premium = True
    elif self.pontuacao < 5:
    self.pontuacao += 1
def diminui_pontuacao(self):
    if self.pontuacao > 1:
        self.pontuacao -=1
        
dani = Pessoa("dani")

print(dani.pontuacao)
dani.aumenta.pontuacao()
print(dani.pontuacao)