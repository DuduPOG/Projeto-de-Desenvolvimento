from models.carro import Carro, Carros
from models.cliente import Cliente, Clientes
from models.detailer import Detailer, Detailers
from models.funileiro import Funileiro, Funileiros
from models.servico import Servico, Servicos
from datetime import datetime


class View:

# Operações iniciais

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

#=======================================================

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

    @staticmethod
    def agendar_servico(data , descrição, funilaria, valor_detailer, valor_funileiro, finalizado, foi_pago, id_cliente, id_detailer, id_funileiro, id_carro):
        servico = Servico(0, data , descrição, funilaria, valor_detailer, valor_funileiro, finalizado, foi_pago, id_cliente, id_detailer, id_funileiro, id_carro)
        Servicos.Inserir(servico)

    @staticmethod
    def listar_servicos_cliente(id):
        servicos_cliente = []
        for servico in View.servicos_listar_todos():
            if servico.get_id_cliente() == id:
                servicos_cliente.append(servico)
        return servicos_cliente

    @staticmethod
    def realizar_pagamento(servico):
        servico.set_pagamento(True)
        Servicos.Atualizar(servico)

#=======================================================

#Operações do Detailer

    @staticmethod
    def detailer_autenticar(email, senha):
        for c in View.detailer_listar_todos():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None
    
    @staticmethod
    def listar_servicos_detailer(id):
        servicos_detailer = []
        for servico in View.servicos_listar_todos():
            if servico.get_id_detailer() == id:
                servicos_detailer.append(id)
        return servicos_detailer
    
    @staticmethod
    def lancar_servico_detailer(servico, valor_detailer, id_funileiro):
        servico.set_funilaria(True)
        servico.set_valor_detailer(valor_detailer)
        servico.set_id_funileiro(id_funileiro)
        Servicos.Atualizar(servico)

    @staticmethod
    def finalizar_servico(servico):
        servico.set_finalizado(True)
        Servicos.Atualizar(servico)

#=======================================================

#Operações do Funileiro
    @staticmethod
    def funileiro_autenticar(email, senha):
        for c in View.funileiro_listar_todos():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None

    @staticmethod
    def listar_servicos_funileiro(id):
        servicos_funileiro = []
        for servico in View.servicos_listar_todos():
            if servico.get_id_funileiro() == id:
                servicos_funileiro.append(id)
        return servicos_funileiro
    
    @staticmethod
    def lancar_servico_funileiro(Servico, valor_detailer):
        Servico.set_valor_funileiro(valor_detailer)
        Servicos.Atualizar(Servico)

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
    def reajustar_valor_servico(servico, novo_preco_detailer, novo_preco_funileiro):
        servico = Servico(servico.get_id(), servico.get_data() , servico.get_desc(), servico.get_funilaria(), novo_preco_detailer, novo_preco_funileiro, servico.get_finalizado(), servico.get_id_cliente(), servico.get_id_detailer(), servico.get_id_funileiro(), servico.get_id_carro())
        Servicos.Atualizar(servico)

#=======================================================

# Operações de Serviço

    @staticmethod
    def servicos_listar_todos():
        return Servicos.Listar()

    @staticmethod
    def servicos_listar_por_id(id):
        return Servicos.Listar_ID(id)

    @staticmethod
    def servico_inserir(data , descrição, funilaria, valor_detailer, valor_funileiro, finalizado, foi_pago, id_cliente, id_detailer, id_funileiro, id_carro):
        servico = Servico(0, data, descrição, funilaria, valor_detailer, valor_funileiro, finalizado, foi_pago, id_cliente, id_detailer, id_funileiro, id_carro)
        Servicos.Inserir(servico)

    @staticmethod
    def servico_excluir(id):
        Serviços = Servicos.Listar_ID(id)
        if Serviços == None:
            return
        else:
            Servicos.Excluir(Serviços)        

#=======================================================

