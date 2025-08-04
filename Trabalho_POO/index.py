import streamlit as st
from view.view import View
from templates.Menu_Admin.mantercarro import ManterCarroUI
from templates.Menu_Admin.mantercliente import ManterClienteUI
from templates.Menu_Admin.manterdetailer import ManterDetailerUI
from templates.Menu_Admin.manterfunileiro import ManterFunileiroUI
from templates.Menu_Visitante.login import LoginUI
from templates.Menu_Visitante.abrirconta import AbrirContaUI
from templates.Menu_Cliente.Cadastrar_Carro import Cadastrar_CarroUI
from templates.Menu_Cliente.agendar_serviçoUI import Agendar_serviçoUI
from templates.Menu_Cliente.Listar_serviços_clientes import ListarserviçosclientesUI
from templates.Menu_Cliente.realizar_pagamentoUI import Realizar_pagamentoUI


class IndexUI:


    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Carros", "Cadastro de Clientes", 
                                  "Cadastro de Detailers", "Cadastro de Funileiros"])
        
        if op == "Cadastro de Carros":
            ManterCarroUI.main()

        if op == "Cadastro de Clientes":
            ManterClienteUI.main()

        if op == "Cadastro de Detailers":
            ManterDetailerUI.main()
            
        if op == "Cadastro de Funileiros":
            ManterFunileiroUI.main()

        #if op == "Cadastro de Serviços":
         #   ManterServicoUI.main()

    def menu_cliente():
        id_cliente = st.session_state.get('cliente_id')
        
        #trocar o carrinho pelo carro do cliente

        """
        if "carrinho_atual" not in st.session_state:
            st.session_state.carrinho_atual = View.iniciar_carrinho(id_cliente)
        """

        op = st.sidebar.selectbox("Menu", ["Cadastrar Carro", "Agendar serviço", 
                                  "Listar meus Serviços", "Realizar pagamento"])

        if op == "Cadastrar Carro" : Cadastrar_CarroUI.main()

        if op == "Agendar serviço" : Agendar_serviçoUI.main()

        if op == "Listar meus Serviços" : ListarserviçosclientesUI.main()

        if op == "Realizar pagamento" : Realizar_pagamentoUI.main()
        
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def sidebar():
        st.write(st.session_state)
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["cliente_nome"] == "admin"
            st.sidebar.write(f"Bem vindo(a), " + st.session_state["cliente_nome"])
            if admin:
                IndexUI.menu_admin()
            #elif st.session_state["cliente_nome"] == "eduardo":
            #    IndexUI.menu_entregador()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()

"""
        
    def menu_detailer():
        op = st.sidebar.selectbox("Menu", ["Listar Minhas Entregas", "Confirmar Entrega"])
        if op == "Listar Minhas Entregas":
            Listar_EntregasUI.main()
        if op == "Confirmar Entrega":
            Confirmar_EntregaUI.main()

    def menu_funileiro():
        op = st.sidebar.selectbox("Menu", ["Listar Minhas Entregas", "Confirmar Entrega"])
        if op == "Listar Minhas Entregas":
            Listar_EntregasUI.main()
        if op == "Confirmar Entrega":
            Confirmar_EntregaUI.main()
"""