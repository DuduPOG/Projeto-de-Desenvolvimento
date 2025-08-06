import streamlit as st
import pandas as pd
from view.view import View
import time

class ReajustarValoresServicosUI:

    @staticmethod
    def main():

        st.header("Reajustar Valor dos Serviços")

        servicos = View.servicos_listar_todos()

        if len(servicos) == 0: 
            st.write("Nenhum Serviço cadastrado")
        else:
            op = st.selectbox("Serviços para reajuste de valor", servicos)
            if op.get_funilaria() == False:
                novo_valor_detailer = st.number_input("Valor do Serviço do Detailer")
                if st.button("Reajustar Valor"):
                    View.reajustar_valor_servico(op, novo_valor_detailer, op.get_valor_funileiro())
                    st.success("Valor reajustado com sucesso")
                    time.sleep(2)
                    st.rerun()
            else:
                novo_valor_detailer = st.number_input("Valor do Serviço do Detailer")
                novo_valor_funileiro = st.number_input("Valor do Serviço do Funileiro")

                if st.button("Reajustar Valor"):
                    View.reajustar_valor_servico(op, novo_valor_detailer, novo_valor_funileiro)
                    st.success("Valor reajustado com sucesso")
                    time.sleep(2)
                    st.rerun()