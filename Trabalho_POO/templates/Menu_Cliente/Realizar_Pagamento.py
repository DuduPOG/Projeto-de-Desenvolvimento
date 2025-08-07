import streamlit as st
import pandas as pd
from view.view import View
import time

class RealizarPagamentoUI:
    
    @staticmethod
    def main():

        st.header("Realizar Pagamento:")

        Servicos = []
        for x in View.servicos_listar_por_id(id_cliente = st.session_state.get('cliente_id')):
            if x.get_pagamento() == True:
                continue
            else:
                Servicos.append(x)

        if len(Servicos) == 0:
            st.write("Você não tem nenhum Serviço pendente de pagamento")
        
        else:
            list_dic = []
            for obj in Servicos:
                dic_x = obj.to_json()

                del dic_x['id']
                del dic_x['valor_funileiro']
                del dic_x['id_cliente']
                del dic_x['id_detailer']
                del dic_x['id_funileiro']
                del dic_x['id_carro']
                
                list_dic.append(dic_x)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

            op = st.selectbox("Selecione o serviço para pagamento", Servicos)

            if st.button("Realizar pagamento"):
                try:
                    View.realizar_pagamento(op)
                    st.success("Pagamento realizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
      