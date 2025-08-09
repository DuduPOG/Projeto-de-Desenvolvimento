import streamlit as st
import pandas as pd
from view.view import View

class ListarServicosFunileiroUI:
    def main():

        st.header("Listar Meus Serviços:")
        
        Servicos = []
        for x in View.servicos_listar_todos():
            if x.get_id_funileiro() == st.session_state.get('funileiro_id') and x.get_finalizado() == False:
                Servicos.append(x)

        if len(Servicos) == 0: 
            st.write("Você não tem nenhum Serviço disponível")
        else:    
            list_dic = []
            for obj in Servicos:
                dic_x = obj.to_json()

                del dic_x['id']
                del dic_x['id_cliente']
                del dic_x['id_detailer']
                del dic_x['id_funileiro']
                del dic_x['id_carro']
                
                list_dic.append(dic_x)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)