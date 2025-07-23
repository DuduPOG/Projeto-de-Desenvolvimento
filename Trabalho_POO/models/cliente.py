from persistencia import CRUD
import json

class Cliente:
    
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

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
    
    def set_email(self, email):
        if email == "":
            raise ValueError("Email não pode ser vazio")
        else:
            self.__email = email

    def get_email(self):
        return self.__email
    
    def set_fone(self, fone):
        if fone == "":
            raise ValueError("Fone não pode ser vazio")
        else:
            self.__fone = fone

    def get_fone(self):
        return self.__fone
    
    def set_senha(self, senha):
        if senha == "":
            raise ValueError("Senha não pode ser vazia")
        else:
            self.__senha = senha

    def get_senha(self):
        return self.__senha
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}"
    
class Clientes(CRUD):

    clientes = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    c = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo)