import streamlit as st
import pandas as pd
from view.view import View
import time

class ListarServicosClienteUI:
    
    @staticmethod
    def main():

        st.header("Listar Meus Serviços:")
        
        Servicos = []
        for x in View.servicos_listar_todos():
            if x.get_id_cliente() == st.session_state.get("cliente_id"):
                Servicos.append(x)

        if len(Servicos) == 0: 
            st.write("Você não tem nenhum Serviço cadastrado")
        else:    
            list_dic = []
            for obj in Servicos:
                dic_x = obj.to_json()

                del dic_x['id']
                del dic_x['valor_funileiro']
                del dic_x['id_cliente']
                
                
                list_dic.append(dic_x)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)