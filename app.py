import streamlit as st
import pandas as pd

# Set the title of the web page
st.set_page_config(page_title="CSV Data Visualizer")
st.title("CSV Data Visualizer")

# 1. File Uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # 2. Load Data with Pandas
    df = pd.read_csv(uploaded_file)
    
    # Show a preview of the data
    st.subheader("Data Preview")
    st.write(df.head())

    # 3. Dynamic Plotting Logic
    st.subheader("Generate Graph")
    
    # Let the user select columns for X and Y axes
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis column", columns)
    y_axis = st.selectbox("Select Y-axis column", columns)

    # 4. Show the Graph
    if st.button("Generate Line Chart"):
        st.line_chart(df.set_index(x_axis)[y_axis])
        
    if st.button("Generate Bar Chart"):
        st.bar_chart(df.set_index(x_axis)[y_axis])

else:
    st.info("Please upload a CSV file to get started.")