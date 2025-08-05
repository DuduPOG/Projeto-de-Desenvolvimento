import streamlit as st
from view.view import View
import time

class FinalizarServicoUI:
    def main():

        st.header("Finalizar meus serviços")

        Serviços = []
        for x in View.servicos_listar_todos():
            if x.get_pagamento() == True:
                continue
            else:
                Serviços.append(x)

        if len(Serviços) == 0:
            st.write("Você não tem nenhum serviço pendente de pagamento")

        op = st.selectbox("Selecione o serviço para finalizar", Serviços)
 
        if st.button("Mandar para funilaria"):
            View.lancar_servico_funileiro(op)
            
        if st.button("finalizar serviço"):
            try:
                View.finalizar_servico()
                st.success("Pagamento realizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
      
        