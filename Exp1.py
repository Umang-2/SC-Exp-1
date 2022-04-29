import streamlit as st
import plotly
import plotly.figure_factory as ff
import plotly.express as px

st.title('Fuzzy Logic : Polynomial Membership Function')
st.write("")
a = st.slider('Value of a:', 1, 10)
b = st.slider('Value of b:', 1, 10)
c = st.slider('Value of c:', 1, 10)

x = [i for i in range(-10,11)]

y=[]
for i in range(len(x)):
    d = x[i]
    y.append(a*(pow(d,2) + b*d + c))

print(x,"\n",y)

st.write('Value of the variables:')
st.write(f'a = {a}')
st.write(f'b = {b}')
st.write(f'c = {c}')

fig = px.line(x = x,y = y, title = 'Polynomial Membership Function')
st.plotly_chart(fig)