import streamlit
import pandas
import requests

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# put a pick list here....
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', fruit_choice)
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screen as a a table
streamlit.dataframe(fruityvice_normalized)


