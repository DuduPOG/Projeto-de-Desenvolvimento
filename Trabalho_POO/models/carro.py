from models.persistencia import CRUD
import json

class Carro:
    
    def __init__(self, id, nome, cor, id_cliente):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cor(cor)
        self.set_id_cliente(id_cliente)

    def to_json(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "cor": self.get_cor(),
            "id_cliente": self.get_id_cliente() 
        }

    def set_id(self, id):
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID precisa ser inteiro e não negativo")
        else:
            self.__id = id

    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode ser vazio")
        else:
            self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_cor(self, cor):
        if cor == "":
            raise ValueError("Cor não pode ser vazia")
        else:
            self.__cor = cor

    def get_cor(self):
        return self.__cor
    pass

    def set_id_cliente(self, id_cliente):
        if not isinstance(id_cliente, int) or id_cliente < 0:
            raise ValueError("ID do cliente precisa ser inteiro e não negativo")
        else:
            self.__id_cliente = id_cliente

    def get_id_cliente(self):
        return self.__id_cliente
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cor} - {self.__id_cliente}"

class Carros(CRUD):

    carros = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("carros.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    c = Carro(dic["id"], dic["nome"], dic["cor"], dic["id_cliente"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("carros.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo)