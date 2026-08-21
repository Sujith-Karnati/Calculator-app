import streamlit as st

st.title("Calculator Application")

st.write('Hello')

number1 = st.number_input('Insert a numer,',value = None,placeholder='enter your first number')
number2 = st.number_input('Insert a numer,',value = None,placeholder='enter your second number')

operation = st.selectbox("select the operation",
                         ('Addition','subtraction','Multiplication','Division'))
ret = st.button("Calculate")

if ret:
    if operation == 'Addition':
        st.write(number1 + number2)
    elif operation == "subtraction":
        st.write(number1-number2)
    elif operation == 'Multiplication':
        st.write(number1*number2)
    elif operation == 'Division':
        st.write(number1/number2)