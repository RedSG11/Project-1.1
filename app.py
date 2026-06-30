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
  st.write(average([1, 2, 3, 4]))
st.logo("Agrisoil Nexus Logo - Emblem Style, Modern Minimalist.png")
st.image("Agrisoil Nexus Logo - Emblem Style, Modern Minimalist.png", caption = "image")
task = st.selectbox("Task", ["Sentiment", "Summarisation", "Q&A"])
thr = st.slider("Threshold", 0.0, 1.0, 1.5)
lang = st.radio("Language", ["VN", "EN"])
if lang == "VN":
  language = "Vietnamese"
else:
  language = "English"
if st.button("Run"):
  st.write("Task: ", task)
  st.write("Threshold: ", thr)
  st.write("In language", language)
st.badge("Approved", color = "green")
st.badge("Reviewing", color = "yellow")
st.markdown(":red-badge[Declined]")
opts = st.multiselect("Select", ["VN", "EN", "FR", "JP", "KR"])
lvl = st.select_slider("Select", ["Low", "Medium", "High"])
if st.button("Say hello"):
  st.write("Hello")
else: 
  st.write("Goodbye")
st.link_button("Open docs", "https://docs.streamlit.io")
st.number_input("Max sentences", max_value = 100, min_value = 1, value = 50)
st.slider("Range", 0.0, 100.0, (25.0, 75.0))
f = st.file_uploader("Upload file", type = ["csv", "txt"])
if f is not None:
  content = f.read()
  st.success("Uploaded")
  st.write(content)
if "messages" not in st.session_state: #Khi vừa chạy session, ko có "messages" nên tạo list tin nhắn trống
  st.session_state.messages = []
prompt = st.chat_input("Ask") #Chat input
if prompt: 
  st.session_state.messages.append({"role" : "user", "content" : prompt}) #Sau khi input, thêm 1 tin nhắn vào list tin nhắn
for m in st.session_state.messages:
  with st.chat_message(m["role"]): #Cứ 1 tin nhắn trong list, tạo khung chat và viết content
    st.write(m["content"])
with st.form("nlp form"):
  st.text_area("Text")
  task = st.selectbox("Task", ["Sentiment", "Summarization", "Q&A"])
  ok = st.form_submit_button("Submit")
if ok:
  st.write(task)
if "count" not in st.session_state:
  st.session_state.count = 0 
if st.button("Increment"):
  st.session_state.count += 1
st.write("Value: ", st.session_state.count)
