import streamlit as st
import time
from view.view import View

class AbrirContaUI:
    def main():
        st.header("Criar conta")
        nome = st.text_input("Seu nome")
        email = st.text_input("Seu e-mail")
        fone = st.text_input("Seu telefone")
        senha = st.text_input("Sua senha", type="password")
        
        if st.button("Criar Conta"):
            try:
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Conta criada com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)