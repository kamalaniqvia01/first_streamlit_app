import streamlit

streamlit.title('Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Kale Smoothie')
streamlit.text('Banana Smoothie')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
