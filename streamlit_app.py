from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.header("Largest among 3 numbers")


num1 = st.number_input('Enter First Numner: ')

num2 = st.number_input('Enter Second Numner: ')

num3 = st.number_input('Enter Third Numner: ')

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

st.write("The Largest Number is ") st.write(largest)


