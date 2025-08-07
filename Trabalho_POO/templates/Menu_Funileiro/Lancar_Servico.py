import streamlit as st
from view.view import View
import time

class LancarServicoFUI:
    def main():

        st.header("Lançar Meus Serviços")

        Servicos = []
        for x in View.servicos_listar_todos():
            if x.get_id_funileiro() == st.session_state.get('funileiro_id') and x.get_finalizado() == False and x.get_funilaria() == True:
                Servicos.append(x)

        if len(Servicos) == 0:
            st.write("Você não tem nenhum Serviço para ser lançado")
        else:
            op = st.selectbox("Selecione o Serviço para lançar", Servicos)
            valor_funileiro = st.number_input("Diga o valor da funilaria: ")
                
            if st.button("Lançar Serviço"):
                try:
                    View.lancar_servico_funileiro(op, valor_funileiro)
                    st.success("Serviço lançado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
      
        