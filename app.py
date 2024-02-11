# packages
import streamlit as st
import pickle

# Assuming doc is a dictionary with a 'page_content' key
def display_doc(doc):
    st.write(doc.page_content.strip())
    st.markdown("---")  # Add a horizontal line for separation

with open("/content/faiss_index.pkl", "rb") as f:
    loaded_index = pickle.load(f)

# Page configuration
st.set_page_config(
    page_title="Sportz Bot",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Main title
st.title("🏆 Welcome to Sportz Bot 🏏")

# Sidebar
st.sidebar.header("🔍 Search About Cricket")

# Text input for the query
query = st.sidebar.text_input("Enter your Test Series 2024 - related query:")

# Button to trigger the search
search_button = st.sidebar.button("Search")

# Display search results when the button is clicked
if search_button and query:
    docs = loaded_index.similarity_search(query)
    st.markdown(f"## 📖 Search Results for '{query}'")
    
    st.markdown(f"## 🏏 Cricket Document")
    # Display each document
    for i, doc in enumerate(docs):
        display_doc(doc)

# Add any additional cricket-themed information or styling as needed
st.sidebar.markdown("---")
st.sidebar.markdown("🏏 Cricket Stats")
st.sidebar.markdown("Total Matches: 5")
st.sidebar.markdown("Top Scorers: Smith, Kohli")
st.sidebar.markdown("Best Bowlers: Bumrah, Ashwin")