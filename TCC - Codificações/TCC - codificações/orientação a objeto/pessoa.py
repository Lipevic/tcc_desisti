## import classes(<- local de ira ser importado) from *(<---- quer dizer tudo)
# ou seja ira importar todas as classes do local
class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

#public, protected(_),private(__)   