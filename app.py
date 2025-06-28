from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

st.title("LLM機能を搭載したWebアプリ")

st.write("##### 動作モード1: 運動")

st.write("##### 動作モード2: 食事")

st.write("選択によって、運動や食事に関する情報を提供します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["運動", "食事"]
)

st.divider()

input_message = ""
if selected_item == "運動":
    input_message = st.text_input(label="運動に関する情報を入力してください。")
    if st.button("実行"):
        if input_message:
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            messages = [
                SystemMessage(content="You are an expert on exercise."),
                HumanMessage(content=input_message),
            ]
        result = llm(messages)
        st.write(result.content)
elif selected_item == "食事":
    input_message = st.text_input(label="食事に関する情報を入力してください。")
    if st.button("実行"):
        if input_message:
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            messages = [
                SystemMessage(content="You are an expert on diet."),
                HumanMessage(content=input_message),
            ]
            result = llm(messages)
        st.write(result.content)
