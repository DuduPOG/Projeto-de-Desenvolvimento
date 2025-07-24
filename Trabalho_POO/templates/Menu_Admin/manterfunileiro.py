import streamlit as st
import pandas as pd
from view.view import View
import time

class ManterFunileiroUI:
    
    @staticmethod
    def main():

        st.header("Cadastro de Funileiros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterFunileiroUI.listar()
        with tab2: ManterFunileiroUI.inserir()
        with tab3: ManterFunileiroUI.atualizar()
        with tab4: ManterFunileiroUI.excluir()

    def listar():

        funileiros = View.funileiro_listar_todos()

        if len(funileiros) == 0: 
            st.write("Nenhum funileiro cadastrado")
        else:    
            list_dic = []
            for obj in funileiros:
                dic_funileiro = obj.to_json()
                del dic_funileiro["senha"]
                list_dic.append(dic_funileiro)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
            
    def inserir():

        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha: ")

        if st.button("Cadastrar"):
            try:

                View.funileiro_inserir(nome, email, fone, senha)
                st.success("Funileiro inserido com sucesso")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.erro(erro)

    def atualizar():

        funileiros = View.funileiro_listar_todos()

        if len(funileiros) == 0: 
            st.write("Nenhum funileiro cadastrado")
        else:
            try:

                op = st.selectbox("Atualização de funileiro", funileiros)
                nome = st.text_input("Informe o novo nome: ", op.get_nome())
                email = st.text_input("Informe o novo e-mail: ", op.get_email())
                fone = st.text_input("Informe o novo fone: ", op.get_fone())

                if st.button("Atualizar"):
                    View.funileiro_atualizar(op.get_id(), nome, email, fone, op.get_senha())
                    st.success("Funileiro atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()

            except ValueError as erro:
                st.error(erro)

    def excluir():

        funileiros = View.funileiro_listar_todos()

        if len(funileiros) == 0: 
            st.write("Nenhum funileiro cadastrado")
        else:

            op = st.selectbox("Exclusão de funileiro", funileiros)

            if st.button("Excluir"):
                View.funileiro_excluir(op.get_id())
                st.success("Funileiro excluído com sucesso")
                time.sleep(2)
                st.rerun()