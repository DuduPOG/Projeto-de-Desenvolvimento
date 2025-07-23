from abc import ABC, abstractmethod

class CRUD(ABC):

    objetos = []

    @classmethod
    def Inserir(cls, obj):
        if cls.objetos:
            maior = max(cliente.get_id() for cliente in cls.objetos)
            obj.set_id(maior + 1)
        else:
            obj.set_id(0)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def Listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def Listar_ID(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()
        else:
            return None

    @classmethod
    def Excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()
        else:
            return None
        """
        if obj not in obj.Listar():
            return None
        else:
            cls.objetos.remove(obj)
            cls.salvar()
        """
    
    @classmethod
    @abstractmethod
    def abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass