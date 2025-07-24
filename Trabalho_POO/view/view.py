from models.carro import Carro, Carros
from models.cliente import Cliente, Clientes
from models.detailer import Detailer, Detailers
from models.funileiro import Funileiro, Funileiros
from models.servico import Servico, Servicos

class View:

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar_todos():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None

    @staticmethod
    def cadastrar_admin():
        for cliente in Clientes.Listar():
            if cliente.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "84911223344","1234")

# Operações do Cliente

    @staticmethod
    def carro_inserir(nome, cor, id_cliente):
        carro = Carro(0, nome, cor, id_cliente)
        Carros.Inserir(carro)

    @staticmethod
    def carro_listar_todos():
        return Carros.Listar()
    
    @staticmethod
    def carro_listar_por_id(id):
        return Carros.Listar_ID(id)
    
    @staticmethod
    def carro_atualizar(id, nome, cor, id_cliente):
        carro = Carro(id, nome, cor, id_cliente)
        Carros.Atualizar(carro)

    @staticmethod
    def carro_excluir(id):
        carro = Carros.Listar_ID(id)
        if carro == None:
            return
        else:
            Carros.Excluir(carro)
#=======================================================
# Operações do Administrador

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        Clientes.Inserir(cliente)

    @staticmethod
    def cliente_listar_todos():
        return Clientes.Listar()
    
    @staticmethod
    def cliente_listar_por_id(id):
        return Clientes.Listar_ID(id)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        Clientes.Atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Clientes.Listar_ID(id)
        if cliente == None:
            return
        else:
            Clientes.Excluir(cliente)

    @staticmethod
    def detailer_inserir(nome, email, fone, senha):
        detailer = Detailer(0, nome, email, fone, senha)
        Detailers.Inserir(detailer)

    @staticmethod
    def detailer_listar_todos():
        return Detailers.Listar()
    
    @staticmethod
    def detailer_listar_por_id(id):
        return Detailers.Listar_ID(id)
    
    @staticmethod
    def detailer_atualizar(id, nome, email, fone, senha):
        detailer = Detailer(id, nome, email, fone, senha)
        Detailers.Atualizar(detailer)

    @staticmethod
    def detailer_excluir(id):
        detailer = Detailers.Listar_ID(id)
        if detailer == None:
            return
        else:
            Detailers.Excluir(detailer)

    @staticmethod
    def funileiro_inserir(nome, email, fone, senha):
        funileiro = Funileiro(0, nome, email, fone, senha)
        Funileiros.Inserir(funileiro)

    @staticmethod
    def funileiro_listar_todos():
        return Funileiros.Listar()
    
    @staticmethod
    def funileiro_listar_id(id):
        return Funileiros.Listar_ID(id)
    
    @staticmethod
    def funileiro_atualizar(id, nome, email, fone, senha):
        funileiro = Funileiro(id, nome, email, fone, senha)
        Funileiros.Atualizar(funileiro)

    @staticmethod
    def funileiro_excluir(id):
        funileiro = Funileiros.Listar_ID(id)
        if funileiro == None:
            return
        else:
            Funileiros.Excluir(funileiro)

    @staticmethod
    def servico_inserir(data, desc, funilaria, valor_detailer, valor_funileiro, finalizado, id_cliente, id_detailer, id_funileiro, id_carro):
        servico = Servico(0, data, desc, funilaria, valor_detailer, valor_funileiro, finalizado, id_cliente, id_detailer, id_funileiro, id_carro)
        Servicos.Inserir(servico)

    @staticmethod
    def servico_listar_todos():
        return Servicos.Listar()
    
    @staticmethod
    def servico_listar_por_id(id):
        return Servicos.Listar_ID(id)
    
    @staticmethod
    def servico_atualizar(id, data, desc, funilaria, valor_detailer, valor_funileiro, finalizado, id_cliente, id_detailer, id_funileiro, id_carro):
        servico = Servico(id, data, desc, funilaria, valor_detailer, valor_funileiro, finalizado, id_cliente, id_detailer, id_funileiro, id_carro)
        Servicos.Atualizar(servico)

    @staticmethod
    def servico_excluir(id):
        servico = Servicos.Listar_ID(id)
        if servico == None:
            return
        else:
            Servicos.Excluir(servico)
#=======================================================