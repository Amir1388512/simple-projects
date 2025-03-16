import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# عنوان اپلیکیشن
st.title('HELLO!')
st.write('This app can get value and show data into a chart.')
st.latex('ax^2 + bx + c')
st.write('👆 this is base for form of my equation ')


a = st.number_input('A : ' , step=1)
b = st.number_input('B : ' , step=1)
c = st.number_input('C : ' , step=1)


x = np.linspace(-10, 10, 200)
y = a * x**2 + b * x + c


fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
ax.set_title('CHART')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

st.pyplot(fig)