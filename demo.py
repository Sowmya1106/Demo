import streamlit as st
st.set_page_config(page_title="cats")
st.markdown("## Types of cats")
col1,col2,col3=st.columns(3)
with col1:
  st.write("- Persian Cat")
  st.image("./download.jpg",width=100,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.write("- White Cat")
  st.image("./pexels-pixabay-104827.jpg",width=100,use_column_width=True)
  st.write("White cats are cute")
with col3: 
  st.write("- Rose")
  st.image("./roses.jpg",width=100,use_column_width=True)
  st.write("Roses are beautiful")
