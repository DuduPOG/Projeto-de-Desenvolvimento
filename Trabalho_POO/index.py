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
from templates.Menu_Detailer.Listar_serviços_detailer import Listar_Entregas_DetailerUI
from templates.Menu_Detailer.Finalizar_serviço import Confirmar_Entrega_detailerUI


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

        op = st.sidebar.selectbox("Menu", ["Cadastrar Carro", "Agendar serviço", 
                                  "Listar meus Serviços", "Realizar pagamento"])

        if op == "Cadastrar Carro" : Cadastrar_CarroUI.main()

        if op == "Agendar serviço" : Agendar_serviçoUI.main()

        if op == "Listar meus Serviços" : ListarserviçosclientesUI.main()

        if op == "Realizar pagamento" : Realizar_pagamentoUI.main()

    def menu_detailer():
        op = st.sidebar.selectbox("Menu", ["Listar Meus serviços", "Finalizar pedido"])

        if op == "Listar Meus serviços":
            Listar_Entregas_DetailerUI.main()
        if op == "Finalizar pedido":
            Confirmar_Entrega_detailerUI.main()

    def menu_funileiro():
        op = st.sidebar.selectbox("Menu", ["Listar Meus serviços", "Finalizar pedido"])
        if op == "Listar Minhas Entregas":
            Listar_EntregasUI.main()
        if op == "Confirmar Entrega":
            Confirmar_EntregaUI.main()
        
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
        
            chaves = [
            "cliente_id",
            "cliente_nome",
            "detailer_nome",
            "detailer_id",
            "funileiro_nome",
            "funileiro_id",
            ]
        
            for chave in chaves:
                if chave in st.session_state:
                    del st.session_state[chave]

        st.rerun()

    def sidebar():
        st.write(st.session_state)

        if "cliente_id" == 0:
            IndexUI.menu_admin()
        
        if "cliente_id" in st.session_state != 0 :
            IndexUI.menu_cliente() 

        if "detailer_id" in st.session_state:
            IndexUI.menu_detailer()

        if "funileiro_id" in st.session_state:
            IndexUI.menu_funileiro()  

        if not("cliente_id" == 0) and not("cliente_id" in st.session_state != 0 ) and not("detailer_id" in st.session_state) and not("funileiro_id" in st.session_state) :
            IndexUI.menu_visitante()
        IndexUI.sair_do_sistema()
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()

