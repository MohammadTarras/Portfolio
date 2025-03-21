import streamlit as st
import pandas as pd
import plotly.express as px

import os
# Page configuration
st.set_page_config(page_title="ML Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Projects", "Model Demo", "Visualizations", "Contact", "Test"])

# Home Page
if page == "Home":
    st.title("Welcome to My Machine Learning Portfolio")
    st.write("This portfolio showcases my ML projects, interactive demos, and insights.")
    st.image("temp/img.jpg", use_container_width=True)

# Projects Page
elif page == "Projects":
    st.title("ML Projects")
    projects = {
        "Predictive Analytics": "A model predicting future trends using time series data.",
        "Image Classification": "A deep learning model classifying images into categories.",
        "Sentiment Analysis": "An NLP model analyzing customer sentiment from text data.",
    }
    for project, description in projects.items():
        st.subheader(project)
        st.write(description)

# Model Demo Page
elif page == "Model Demo":
    st.title("Live Model Demo")
    st.write("Enter data below and see the model's predictions in real-time.")
    
    # Example input fields
    feature1 = st.slider("Feature 1", 0.0, 10.0, 5.0)
    feature2 = st.slider("Feature 2", 0.0, 10.0, 5.0)
    
    # Placeholder model logic (replace with actual model)
    prediction = (feature1 + feature2) / 2
    st.write(f"Predicted Value: {prediction:.2f}")

# Visualizations Page
elif page == "Visualizations":
    st.title("Data Visualizations")
    
    # Sample Data
    df = pd.DataFrame({
        "Category": ["A", "B", "C", "D", "E"],
        "Values": [10, 20, 15, 25, 30]
    })
    
    # Bar Chart
    st.subheader("Bar Chart")
    fig_bar = px.bar(df, x="Category", y="Values", title="Category-wise Values")
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Line Chart
    st.subheader("Line Chart")
    fig_line = px.line(df, x="Category", y="Values", title="Category Trends", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Scatter Plot
    st.subheader("Scatter Plot")
    fig_scatter = px.scatter(df, x="Category", y="Values", title="Scatter Representation")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out via LinkedIn or email for collaborations!")
    st.write("Email: your.email@example.com")
    st.write("LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)")
# Contact Page
elif page == "Test":
    st.title("Filtering a DataFrame!")
    # Create sample data
    data = {
        "Customer Name": [
            "John Doe", "John Doe", "John Doe",
            "Jane Smith", "Jane Smith",
            "Alice Johnson", "Alice Johnson", "Alice Johnson",
            "Bob Brown",
            "Charlie White", "Charlie White"
        ],
        "Product": [
            "Laptop", "Smartphone", "Tablet",
            "Smartphone", "Tablet",
            "Laptop", "Headphones", "Smartwatch",
            "Headphones",
            "Smartphone", "Smartwatch"
        ],
        "Quantity": [2, 1, 3, 1, 2, 1, 5, 2, 4, 1, 3]
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    filter_on = st.selectbox("Filter on", df['Customer Name'].unique())
    st.write(df[df['Customer Name'] == filter_on])
    st.write(f"Sum of sales for {filter_on}: {df[df['Customer Name'] == filter_on]['Quantity'].sum()}")


