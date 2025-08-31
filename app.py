import streamlit as st

# Streamlit UI
st.title("POWER CALCULATOR")
st.write("Enter a number to calculate it's square, cube, fifth power")

#Get user input
n = st.number_input("Enter an integer: ", value=1, step=1)

# calculate
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The square is {square}")
st.write(f"The cube is {cube}")
st.write(f"The fifth power is {fifth_power}")