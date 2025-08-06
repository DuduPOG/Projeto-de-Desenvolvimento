import streamlit as st
from view.view import View
from templates.Menu_Admin.mantercarro import ManterCarroUI
from templates.Menu_Admin.mantercliente import ManterClienteUI
from templates.Menu_Admin.manterdetailer import ManterDetailerUI
from templates.Menu_Admin.manterfunileiro import ManterFunileiroUI
from templates.Menu_Visitante.login import LoginUI
from templates.Menu_Visitante.abrirconta import AbrirContaUI
from templates.Menu_Cliente.Cadastrar_Carro import ManterCarroUI
from templates.Menu_Cliente.Agendar_Servico import AgendarServicoUI
from templates.Menu_Cliente.Listar_Servicos_Cliente import ListarServicosClienteUI
from templates.Menu_Cliente.Realizar_Pagamento import RealizarPagamentoUI
from templates.Menu_Detailer.Listar_Servicos_Detailer import ListarServicosDetailerUI
from templates.Menu_Detailer.Lancar_Servico import LancarServicoDUI
from templates.Menu_Detailer.Finalizar_Servico import FinalizarServicoUI
from templates.Menu_Funileiro.Listar_Servicos_Funileiro import ListarServicosFunileiroUI
from templates.Menu_Funileiro.Lancar_Servico import LancarServicoFUI


class IndexUI:


    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", 
                                  "Cadastro de Detailers", "Cadastro de Funileiros"])

        if op == "Cadastro de Clientes":
            ManterClienteUI.main()

        if op == "Cadastro de Detailers":
            ManterDetailerUI.main()
            
        if op == "Cadastro de Funileiros":
            ManterFunileiroUI.main()

    def menu_cliente():

        op = st.sidebar.selectbox("Menu", ["Cadastrar Carro", "Agendar Serviço", 
                                  "Listar Meus Serviços", "Realizar Pagamento"])

        if op == "Cadastrar Carro" : ManterCarroUI.main()

        if op == "Agendar Serviço" : AgendarServicoUI.main()

        if op == "Listar Meus Serviços" : ListarServicosClienteUI.main()

        if op == "Realizar Pagamento" : RealizarPagamentoUI.main()

    def menu_detailer():
        op = st.sidebar.selectbox("Menu", ["Listar Meus Serviços", "Lançar Serviço", "Finalizar Serviço"])

        if op == "Listar Meus Serviços":
            ListarServicosDetailerUI.main()

        if op == "Lançar Serviço":
            LancarServicoDUI.main()

        if op == "Finalizar Serviço":
            FinalizarServicoUI.main()

    def menu_funileiro():
        op = st.sidebar.selectbox("Menu", ["Listar Meus Serviços", "Lançar Serviço"])

        if op == "Listar Minhas Serviços":
            ListarServicosFunileiroUI.main()

        if op == "Lançar Serviço":
            LancarServicoFUI.main()
        
    
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

