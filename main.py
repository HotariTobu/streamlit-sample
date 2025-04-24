import streamlit as st
import time

st.write("Hello world")

uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file is not None:
    st.write(uploaded_file)


@st.dialog("Hello!")
def hello():
    st.write("Hello from the dialog!")


if st.button("Open dialog"):
    hello()

with st.sidebar:
    st.write("This is the sidebar")

if st.button("Click me!"):
    st.toast("Button clicked!")

data = [
    {"Name": "Alice", "Age": 30},
    {"Name": "Bob", "Age": 25},
    {"Name": "Charlie", "Age": 35},
    {"Name": "David", "Age": 28},
    {"Name": "Eve", "Age": 22},
    {"Name": "Frank", "Age": 40},
    {"Name": "Grace", "Age": 29},
    {"Name": "Heidi", "Age": 31},
    {"Name": "Ivan", "Age": 27},
    {"Name": "Judy", "Age": 26},
    {"Name": "Karl", "Age": 33},
    {"Name": "Leo", "Age": 24},
]

st.dataframe(data)

edited_data = st.data_editor(data, num_rows="dynamic")
if st.button("Save changes"):
    print(edited_data)
    st.write("Changes saved!")

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)


def main():
    st.write("This is the main function")
    print("Hello from streamit-sample!")


if __name__ == "__main__":
    main()
