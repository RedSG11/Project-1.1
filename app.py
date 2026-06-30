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
st.write("write?")
