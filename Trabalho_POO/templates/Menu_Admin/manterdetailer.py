import streamlit as st
import pandas as pd
from view import View
import time

class ManterDetailerUI:
    
    @staticmethod
    def main():
        st.header("Cadastro de Detailers")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterDetailerUI.listar()
        with tab2: ManterDetailerUI.inserir()
        with tab3: ManterDetailerUI.atualizar()
        with tab4: ManterDetailerUI.excluir()

    def listar():

        detailers = View.detailer_listar_todos()

        if len(detailers) == 0: 
            st.write("Nenhum detailer cadastrado")
        else:    
            list_dic = []
            for obj in detailers:
                dic_detailer = obj.to_json()
                del dic_detailer["senha"]
                list_dic.append(dic_detailer)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
            
    def inserir():

        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha: ")

        if st.button("Cadastrar"):
            try:

                View.detailer_inserir(nome, email, fone, senha)
                st.success("Detailer inserido com sucesso")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.erro(erro)

    def atualizar():

        detailers = View.detailer_listar_todos()

        if len(detailers) == 0: 
            st.write("Nenhum detailer cadastrado")
        else:
            try:

                op = st.selectbox("Atualização de detailer", detailers)
                nome = st.text_input("Informe o novo nome: ", op.get_nome())
                email = st.text_input("Informe o novo e-mail: ", op.get_email())
                fone = st.text_input("Informe o novo fone: ", op.get_fone())

                if st.button("Atualizar"):
                    View.cliente_atualizar(op.get_id(), nome, email, fone, op.get_senha())
                    st.success("Detailer atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()

            except ValueError as erro:
                st.error(erro)

    def excluir():

        detailers = View.detailer_listar_todos()

        if len(detailers) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:

            op = st.selectbox("Exclusão de cliente", detailers)

            if st.button("Excluir"):
                View.detailer_excluir(op.get_id())
                st.success("Detailer excluído com sucesso")
                time.sleep(2)
                st.rerun()