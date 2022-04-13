# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:07:45 2022

@author: Bibek77
"""

import streamlit as st
import pandas as pd
import numpy as np# Core Pkgs
import streamlit as st
import dtale

# EDA Pkgs
import pandas as pd
import codecs
from pandas_profiling import ProfileReport

# Components Pkgs
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report

# Custome Component Fxn
import sweetviz as sv
import streamlit.components.v1 as components
from dtale.views import startup
from dtale.app import get_instance

CSS = """
"""

def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)



def main():




	"""A Simple EDA App with Streamlit Components"""

	menu = ["Home","Pandas Profile","Sweetviz","Dtale"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Pandas Profile":
		st.subheader("Automated EDA with Pandas Profile")
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.dataframe(df.head())
			profile = ProfileReport(df)
			st_profile_report(profile)


	elif choice == "Sweetviz":
		st.subheader("Automated EDA with Sweetviz")
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.dataframe(df.head())
			if st.button("Generate Sweetviz Report"):

				# Normal Workflow
				report = sv.analyze(df)
				report.show_html()
				st_display_sweetviz("SWEETVIZ_REPORT.html")
				

	elif choice == "Dtale":
		st.title("Automated EDA with Dtale")
		
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.dataframe(df.head())
			st.subheader('Please click the play button which is in  top-left corner  for more features')
			startup(data_id="1", data=df)
			curr_instance = get_instance("1")
		html = f"""
			{CSS}
		<iframe src="/dtale/main/1" style="height: 600px ;width: 100%"/>
		"""

		st.markdown(html, unsafe_allow_html=True)	

	else:
		st.subheader("Home")
		html_temp = """

		<h1 style="color:white;text-align:center;">Simple EDA App </h1>
		</div>
		"""

		# components.html("<p style='color:red;'> Streamlit Components is Awesome</p>")
		components.html(html_temp)






if __name__ == '__main__':
	main()