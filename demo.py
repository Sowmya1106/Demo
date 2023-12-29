import streamlit as st
st.set_page_config(page_title="cats")
st.markdown("## Types of cats")
col1,col2=st.columns(2)
with col1:
st.write("- Persian Cat")
st.image("./download.jpg",width=100,use_column_width=True)
with col2:
st.write("- White Cat")
st.image("./pexels-pixabay-104827.jpg",width=100,use_column_width=True)
st.write("- Rose")
st.image("./roses.jpg",width=100,use_column_width=True)
