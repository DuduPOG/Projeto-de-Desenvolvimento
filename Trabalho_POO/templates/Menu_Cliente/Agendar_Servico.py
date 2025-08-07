import streamlit as st
from view.view import View
import time 
from datetime import datetime


class AgendarServicoUI:
    
    @staticmethod
    def main():

        st.header("Agendar Serviço")
      
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
        carros = View.carro_listar_todos()
        meus_carros = []
        for carro in carros:
            if carro.get_id_cliente() == st.session_state.get('cliente_id'):
                meus_carros.append(carro)
        op = st.selectbox("Selecione o Carro", meus_carros)   
        id_carro = op.get_id() 


        if st.button("Agendar Serviço"):
            try:
                id_cliente = int(id_cliente)
                View.agendar_servico(data , descrição, funilaria, valor_detailer, valor_funileiro, finalizado, foi_pago, id_cliente, id_detailer, id_funileiro, id_carro)
                st.success("Agendamento concluído com sucesso")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.error(erro)