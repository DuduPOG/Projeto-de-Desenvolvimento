from models.persistencia import CRUD
from datetime import datetime
import json

class Servico:

    def __init__(self, id, data, desc, funilaria, valor_detailer, valor_funileiro, finalizado, foi_pago, id_cliente, id_detailer, id_funileiro, id_carro):
        self.set_id(id)
        self.set_data(data)
        self.set_desc(desc)
        self.set_funilaria(funilaria)
        self.set_valor_detailer(valor_detailer)
        self.set_valor_funileiro(valor_funileiro)
        self.set_finalizado(finalizado)
        self.set_pagamento(foi_pago)
        self.set_id_cliente(id_cliente)
        self.set_id_detailer(id_detailer)
        self.set_id_funileiro(id_funileiro)
        self.set_id_carro(id_carro)

    def to_json(self):
        return {
            "id": self.get_id(),
            "data": self.get_data(),
            "desc": self.get_desc(),
            "funilaria": self.get_funilaria(),
            "valor_detailer": self.get_valor_detailer(),
            "valor_funileiro": self.get_valor_funileiro(),
            "valor_servico": self.get_valor_servico(),
            "finalizado": self.get_finalizado(),
            "foi_pago": self.get_pagamento(),
            "id_cliente": self.get_id_cliente(),
            "id_detailer": self.get_id_detailer(),
            "id_funileiro": self.get_id_funileiro(),
            "id_carro": self.get_id_carro()
        }

    def set_id(self, id):
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID precisa ser inteiro e não negativo")
        else:
            self.__id = id

    def get_id(self):
        return self.__id
    
    def set_data(self, data):
        if data == "":
            raise ValueError("Data não pode ser vazia e precisa ser do tipo data")
        else:
            self.__data = data

    def get_data(self):
        return self.__data 
    
    def set_desc(self, desc):
        if desc == "":
            raise ValueError("Descrição não pode ser vazia")
        else:
            self.__desc = desc

    def get_desc(self):
        return self.__desc
    
    def set_funilaria(self, funilaria):
        if not isinstance(funilaria, bool) or funilaria == "":
            raise ValueError("Funilaria não pode ser vazio e deve ser um valor lógico")
        else:
            self.__funilaria = funilaria

    def get_funilaria(self):
        return self.__funilaria
    
    def set_valor_detailer(self, valor_detailer):
        if not isinstance(valor_detailer, float) or valor_detailer == "":
            raise ValueError("Valor do detailer não pode ser vazio e precisa ser real")
        else:
            self.__valor_detailer = valor_detailer

    def get_valor_detailer(self):
        return self.__valor_detailer
    
    def set_valor_funileiro(self, valor_funileiro):
        if not isinstance(valor_funileiro, float) or valor_funileiro == "":
            raise ValueError("Valor do funileiro não pode ser vazio e precisa ser real")
        else:
            self.__valor_funileiro = valor_funileiro

    def get_valor_funileiro(self):
        return self.__valor_funileiro
    
    def get_valor_servico(self):
        if self.__funilaria == False:
            return self.__valor_detailer
        return self.__valor_detailer + self.__valor_funileiro
    
    def set_finalizado(self, finalizado):
        if not isinstance(finalizado, bool) or finalizado == "":
            raise ValueError("Finalizado não pode ser vazio e deve ser um valor lógico")
        else:
            self.__finalizado = finalizado

    def set_pagamento(self, foi_pago):
        if not isinstance(foi_pago, bool) or foi_pago == "":
            raise ValueError("A confirmação do pagamento não pode ser vazia e deve ser um valor lógico")
        else:
            self.__foi_pago = foi_pago

    def get_pagamento(self):
        return self.__foi_pago

    def get_finalizado(self):
        return self.__finalizado

    def set_id_cliente(self, id_cliente):
        if not isinstance(id_cliente, int) or id_cliente < 0:
            raise ValueError("ID do cliente precisa ser inteiro e não negativo")
        else:
            self.__id_cliente = id_cliente

    def get_id_cliente(self):
        return self.__id_cliente
    
    def set_id_detailer(self, id_detailer):
        if not isinstance(id_detailer, int) or id_detailer < 0:
            raise ValueError("ID do detailer precisa ser inteiro e não negativo")
        else:
            self.__id_detailer = id_detailer

    def get_id_detailer(self):
        return self.__id_detailer
    
    def set_id_funileiro(self, id_funileiro):
        if not isinstance(id_funileiro, int) or id_funileiro < 0:
            raise ValueError("ID do funileiro precisa ser inteiro e não negativo")
        else:
            self.__id_funileiro = id_funileiro

    def get_id_funileiro(self):
        return self.__id_funileiro
    
    def set_id_carro(self, id_carro):
        if not isinstance(id_carro, int) or id_carro < 0:
            raise ValueError("ID do carro precisa ser inteiro e não negativo")
        else:
            self.__id_carro = id_carro

    def get_id_carro(self):
        return self.__id_carro
    pass

    def __str__(self):
        if self.__funilaria == False:
            return f"{self.__id} - {self.__data} - {self.__desc} - {self.__funilaria} - {self.get_valor_servico()} - {self.__finalizado} - {self.__foi_pago} - {self.__id_cliente} - {self.__id_detailer} - {self.__id_carro}"
        else:
            return f"{self.__id} - {self.__data} - {self.__desc} - {self.__funilaria} - {self.__valor_detailer} - {self.__valor_funileiro} - {self.get_valor_servico()} - {self.__finalizado} - {self.__foi_pago} - {self.__id_cliente} - {self.__id_detailer} - {self.__id_funileiro} - {self.__id_carro}"

class Servicos(CRUD):

    servicos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    c = Servico(dic["id"], dic["data"], dic["desc"], dic["funilaria"], dic["valor_detailer"],
                                dic["valor_funileiro"], dic["finalizado"], dic["foi_pago"], dic["id_cliente"],
                                dic["id_detailer"], dic["id_funileiro"], dic["id_carro"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo)