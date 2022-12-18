import streamlit as st

def custombg():
  page = """
  <style>
  [data-testid="stAppViewContainer"]{
  background: rgb(17,7,215);
  background: -moz-linear-gradient(90deg, rgba(17,7,215,1) 0%, rgba(6,115,210,1) 100%);
  background: -webkit-linear-gradient(90deg, rgba(17,7,215,1) 0%, rgba(6,115,210,1) 100%);
  background: linear-gradient(90deg, rgba(17,7,215,1) 0%, rgba(6,115,210,1) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#1107d7",endColorstr="#0673d2",GradientType=1);
  }

  [data-testid="stVerticalBlock"]{
  /* From https://css.glass */
  background: rgba(255, 255, 255, 0.09);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  padding: 2rem;
  # width: 100%;
  }

  [data-testid="stVerticalBlock"] p{
    width: 90%;
  }

  [data-testid="stHeader"]{
  background: rgb(23,14,200);
  background: linear-gradient(150deg, rgba(23,14,200,1) 34%, rgba(1,167,200,1) 100%);
  }

  .css-6qob1r{
  /* From https://css.glass */
  background-color: #1544df90;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  }

  .css-6qob1r [data-testid="stVerticalBlock"]{
    background-color: transparent;
  }

  </style>
  """

  st.markdown(page, unsafe_allow_html=True)