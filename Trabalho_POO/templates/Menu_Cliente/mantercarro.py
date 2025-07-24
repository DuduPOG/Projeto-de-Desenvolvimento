import streamlit as st
import pandas as pd
from view.view import View
import time

class ManterCarroUI:
    
    @staticmethod
    def main():

        st.header("Cadastro de Carros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCarroUI.listar()
        with tab2: ManterCarroUI.inserir()
        with tab3: ManterCarroUI.atualizar()
        with tab4: ManterCarroUI.excluir()

    def listar():

        carros = View.carro_listar_todos()

        if len(carros) == 0: 
            st.write("Nenhum carro cadastrado")
        else:    
            list_dic = []
            for obj in carros:
                dic_carro = obj.to_json()
                list_dic.append(dic_carro)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
            
    def inserir():

        nome = st.text_input("Informe o nome: ")
        cor = st.text_input("Informe a cor: ")
        id_cliente = st.text_input("Informe o id do proprietário: ")

        if st.button("Cadastrar"):
            try:
                id_cliente = int(id_cliente)
                View.carro_inserir(nome, cor, id_cliente)
                st.success("Carro inserido com sucesso")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.erro(erro)

    def atualizar():

        carros = View.carro_listar_todos()

        if len(carros) == 0: 
            st.write("Nenhum carro cadastrado")
        else:
            try:

                op = st.selectbox("Atualização de carro", carros)
                nome = st.text_input("Informe o novo nome: ", op.get_nome())
                cor = st.text_input("Informe a nova cor: ", op.get_email())
                id_cliente = st.text_input("Reinforme o id do proprietário (número inteiro não negativo): ", op.get_id_cliente())

                if st.button("Atualizar"):
                    id_cliente = int(id_cliente)
                    View.carro_atualizar(op.get_id(), nome, cor, id_cliente)
                    st.success("Carro atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()

            except ValueError as erro:
                st.error(erro)

    def excluir():

        carros = View.carro_listar_todos()

        if len(carros) == 0: 
            st.write("Nenhum carro cadastrado")
        else:
            op = st.selectbox("Exclusão de carro", carros)
            
            if st.button("Excluir"):
                View.carro_excluir(op.get_id())
                st.success("Carro excluído com sucesso")
                time.sleep(2)
                st.rerun()