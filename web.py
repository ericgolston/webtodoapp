import streamlit as st
import functions # Backend adds get todos and write todos

todos = functions.get_todos() # Has default argument; Creates list from todos.txt file
def add_todo():
	todo = '\n' + st.session_state['new_todo']
	todos.append(todo) # Global Variable
	functions.write_todos(todos)





st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
	checkbox = st.checkbox(todo, key=todo)
	if checkbox:  #If checkbox is True
		todos.pop(index) # pop todos out of list at index
		functions.write_todos(todos)
		del st.session_state[todo]
		st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo. . . ",
			  on_change=add_todo, key='new_todo')

