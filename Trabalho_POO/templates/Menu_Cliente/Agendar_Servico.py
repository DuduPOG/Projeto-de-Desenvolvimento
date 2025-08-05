import streamlit as st
from view.view import View
import time 
from datetime import datetime


class AgendarServicoUI:
    
    @staticmethod
    def main():

        st.header("Agendar Serviço")
        tab1, tab2 = st.tabs(["Iniciar Serviço", "Excluir"])
        with tab1: AgendarServicoUI.inserir()
        with tab2: AgendarServicoUI.excluir()
      
    def inserir():
        data = time.strftime("%Y-%m-%d %H:%M:%S")
        descrição = st.text_input("Descrição do Serviço: ")
        funilaria = False
        valor_detailer = 0.0
        valor_funileiro = 0.0
        finalizado = False
        foi_pago = False
        id_cliente = st.session_state.get('cliente_id')
        id_detailer = 0
        id_funileiro = 0
        carro = st.selectbox("Selecione o Carro", View.listar_carros_por_id( st.session_state.get('cliente_id')))   
        id_carro = carro.get_id() 


        if st.button("Agendar Serviço"):
            try:
                id_cliente = int(id_cliente)
                View.serviço_inserir(data , descrição, funilaria, valor_detailer, valor_funileiro, finalizado, foi_pago, id_cliente, id_detailer, id_funileiro, id_carro)
                st.success("Agendamento concluído com sucesso")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.error(erro)

    def excluir():

        Serviços = View.servicos_listar_por_id(id_cliente = st.session_state.get('cliente_id'))

        if len(Serviços) == 0: 
            st.write("Nenhum Serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviço", Serviços)
            
            if st.button("Excluir"):
                View.Serviços_excluir(op.get_id())
                st.success("Carro excluído com sucesso")
                time.sleep(2)
                st.rerun()