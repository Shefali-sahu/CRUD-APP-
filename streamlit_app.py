import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"  # FastAPI server

st.set_page_config(page_title="Books CRUD App", page_icon="📚", layout="wide")
st.title("📚 Books CRUD App (FastAPI + PostgreSQL + Streamlit)")

# --- Load All Books ---
st.header("📖 All Books")
if st.button("Load Books"):
    response = requests.get(f"{API_URL}/books/")
    if response.status_code == 200:
        books = response.json()
        if books:
            df = pd.DataFrame(books)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No books found. Add some!")
    else:
        st.error(f"❌ Failed to fetch books: {response.text}")


# --- Create New Book ---
st.header("➕ Add New Book")
with st.form("create_book_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    description = st.text_area("Description")
    year = st.number_input("Year", min_value=0, step=1)
    submitted = st.form_submit_button("Create Book")

    if submitted:
        data = {"title": title, "author": author, "description": description, "year": year}
        response = requests.post(f"{API_URL}/books/", json=data)
        if response.status_code == 200:
            st.success("✅ Book created successfully!")
        else:
            st.error(f"❌ Failed to create book: {response.text}")


# --- Get Book by ID ---
st.header("🔎 Get Book by ID")
book_id = st.number_input("Enter Book ID", min_value=1, step=1)
if st.button("Get Book"):
    response = requests.get(f"{API_URL}/books/{book_id}")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("❌ Book not found")


# --- Update Book ---
st.header("✏️ Update Book")
with st.form("update_book_form"):
    update_id = st.number_input("Book ID to update", min_value=1, step=1)
    new_title = st.text_input("New Title")
    new_author = st.text_input("New Author")
    new_description = st.text_area("New Description")
    new_year = st.number_input("New Year", min_value=0, step=1)
    update_submit = st.form_submit_button("Update Book")

    if update_submit:
        data = {
            "title": new_title,
            "author": new_author,
            "description": new_description,
            "year": new_year
        }
        response = requests.put(f"{API_URL}/books/{update_id}", json=data)
        if response.status_code == 200:
            st.success("✅ Book updated!")
        else:
            st.error(f"❌ Failed to update book: {response.text}")


# --- Delete Book ---
st.header("🗑️ Delete Book")
delete_id = st.number_input("Book ID to delete", min_value=1, step=1)
if st.button("Delete Book"):
    response = requests.delete(f"{API_URL}/books/{delete_id}")
    if response.status_code == 200:
        st.success("✅ Book deleted!")
    else:
        st.error("❌ Failed to delete book")
