# Core Pkgs
import streamlit as st 

# Utils Pkgs
import codecs

# Components Pkgs
import streamlit.components.v1 as components

# Custom Components Fxn
def st_calculator(calc_html,width=700,height=700):
	calc_file = codecs.open(calc_html,'r')
	page = calc_file.read()
	components.html(page,width=width,height=height,scrolling=False)


def main():
	"""A Calculator App with Streamlit Components"""

	menu = ["Calculator"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Calculator":
		
		st.subheader("Calculator")
		# components.html(html_temp)
		st_calculator('./components/calculator/calculator.html')


if __name__ == '__main__':
	main()