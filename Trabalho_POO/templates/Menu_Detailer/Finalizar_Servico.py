import streamlit as st
from view.view import View
import time

class FinalizarServicoUI:
    def main():

        st.header("Finalizar Meus Serviços")

        Servicos = []
        for x in View.servicos_listar_todos():
            if x.get_finalizado() == False:
                Servicos.append(x)

        if len(Servicos) == 0:
            st.write("Você não tem nenhum Serviço inconcluído")
        else:
            op = st.selectbox("Selecione o Serviço para finalizar", Servicos)
                
            if st.button("Finalizar Serviço"):
                try:
                    View.finalizar_servico(op)
                    st.success("Serviço finalizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
      
        