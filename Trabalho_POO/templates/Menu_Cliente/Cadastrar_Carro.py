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
        Carros = []
        for carros in View.carro_listar_todos():
            if carros.get_id_cliente() == st.session_state.get('cliente_id'):
                Carros.append(carros)

        if len(Carros) == 0: 
            st.write("Você não tem nenhum Carro cadastrado")
        else:    
            list_dic = []
            for obj in Carros:
                dic_carro = obj.to_json()

                del dic_carro['id_cliente']
                del dic_carro['id']

                list_dic.append(dic_carro)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
            
    def inserir():

        nome = st.text_input("Informe o nome: ")
        cor = st.text_input("Informe a cor: ")
        id_cliente = st.session_state.get('cliente_id')

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
        meus_carros = []
        for carro in carros:
            if carro.get_id_cliente() == st.session_state.get('cliente_id'):
                meus_carros.append(carro)

        if len(meus_carros) == 0: 
            st.write("Nenhum Carro cadastrado")
        else:
            try:

                op = st.selectbox("Atualização de Carro", meus_carros)
                nome = st.text_input("Informe o novo nome: ", op.get_nome())
                cor = st.text_input("Informe a nova cor: ", op.get_cor())
                id_cliente = st.session_state.get('cliente_id')

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
        meus_carros = []
        for carro in carros:
            if carro.get_id_cliente() == st.session_state.get('cliente_id'):
                meus_carros.append(carro)

        if len(meus_carros) == 0: 
            st.write("Nenhum Carro cadastrado")
        else:
            op = st.selectbox("Exclusão de Carro", meus_carros)
            
            if st.button("Excluir"):
                View.carro_excluir(op.get_id())
                st.success("Carro excluído com sucesso")
                time.sleep(2)
                st.rerun()