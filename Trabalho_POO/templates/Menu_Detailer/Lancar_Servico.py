import streamlit as st
from view.view import View
import time

class LancarServicoDUI:
    def main():

        st.header("Lançar Meus Serviços")

        Servicos = []
        for x in View.servicos_listar_todos():
            if x.get_id_detailer() == st.session_state.get('detailer_id') and x.get_finalizado() == False:
                Servicos.append(x)

        if len(Servicos) == 0:
            st.write("Você não tem nenhum Serviço para ser lançado")
        else:
            op = st.selectbox("Selecione o Serviço para lançar", Servicos)
    
            valor_detailer = st.number_input("Diga o valor do serviço: ")

            op2 = st.selectbox("Selecione o funileiro: ", View.funileiro_listar_todos())
            
        if st.button("Lançar Serviço"):
            try:
                View.lancar_servico_detailer(op, valor_detailer, op2.get_id())
                st.success("Serviço lançado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
      
        