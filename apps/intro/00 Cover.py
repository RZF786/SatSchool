import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import json

logo = True

with open ('apps/intro/satschoollottie.json', 'r') as f:
    lottie_satschool = json.load(f)
    
st.title('SatSchool - Hands on with Data')

st.markdown("""
    <style>
.button-30 {
  align-items: center;
  appearance: none;
  background-color: #FCFCFD;
  border-radius: 4px;
  border-width: 0;
  box-shadow: rgba(45, 35, 66, 0.4) 0 2px 4px,rgba(45, 35, 66, 0.3) 0 7px 13px -3px,#D6D6E7 0 -3px 0 inset;
  box-sizing: border-box;
  color: #36395A;
  cursor: pointer;
  display: inline-flex;
  font-family: "JetBrains Mono",monospace;
  height: 48px;
  justify-content: center;
  line-height: 1;
  list-style: none;
  overflow: hidden;
  padding-left: 16px;
  padding-right: 16px;
  position: relative;
  text-align: left;
  text-decoration: none;
  transition: box-shadow .15s,transform .15s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  will-change: box-shadow,transform;
  font-size: 18px;
}

.button-30:focus {
  box-shadow: #D6D6E7 0 0 0 1.5px inset, rgba(45, 35, 66, 0.4) 0 2px 4px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #D6D6E7 0 -3px 0 inset;
}

.button-30:hover {
  box-shadow: rgba(45, 35, 66, 0.4) 0 4px 8px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #D6D6E7 0 -3px 0 inset;
  transform: translateY(-2px);
}

.button-30:active {
  box-shadow: #D6D6E7 0 3px 7px inset;
  transform: translateY(2px);
}
    </style>
    """, unsafe_allow_html=True)

url = 'https://forms.gle/SGnSzT6DhR1y3Cp97'
st.markdown(f"#### <a href='{url}'><button class='button-30' role='button'>Provide feedback here</button></a>", unsafe_allow_html=True)

a,b = st.columns([0.3,0.5])

with a:
    st_lottie(lottie_satschool, key="lottie_satschool", speed=0.5, loop=False, quality='high', width=400)
   
b.markdown("""Welcome to the 'Hands on with Data' module as part of SatSchool. 🚀🚀🚀

For the main SatSchool website, please visit **[https://satschool-outreach.github.io](https://satschool-outreach.github.io)**.



In this module you will learn how to manipulate and understand data from satellites in a range of environmental contexts. It's your chance to get hands on with satellite data!

You will learn:

* How scientists work with satellite data to better understand different parts of the Earth system
* How to work with different kinds of satellite data yourself and the types of information it contains
* How to interpret maps and graphs displaying different types of environmental data

<img src="https://www.gim-international.com/cache/a/f/b/3/2/afb32cbe5b80419c8de0d63398cfb5c661498273.jpeg" alt="Sentinel 2" width="700">""", unsafe_allow_html=True)
