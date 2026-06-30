import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import io 
from PIL import Image 
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Normal text")
st.markdown("**Bold** and *Italic*")
st.latex(r"P(A | B) = \frac{P(B | A) * P(A)}{P(B)}")
st.write("write")
st.code("def average(list): return sum(list)/len(list)", language = "python")
with st.echo():
  def average(list): 
    return sum(list)/len(list)
  print(average([1, 2, 3, 4]))
