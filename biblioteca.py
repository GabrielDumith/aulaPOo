class Pessoa():
     def __init__(self,nome, peso,idade):
        self.nome= nome
        self.peso = peso
        self.idade = idade
        self.dormindo = False
        self.comendo = False
        self.falando = False

     def Comer(self):
        if self.falando:
            print("nao pode falar enquanto come")
        elif self.dormindo:
            print("nao pode comer enquanto dormindo")
        elif self.dormindo:
            print("ja esta dormindo")
        else:
            self.comendo= True
            print(f"{self.nome} esta dormindo")
    def dormir(self):
        if self.falando

