import streamlit as st
import requests
st.title("world info search 🗺️")
inp=st.text_input("Enter country's name: ")
if "country"not in st.session_state:
   st.session_state.country=[]

nd1np=inp.lower()
url=f"https://restcountries.com/v3.1/name/{nd1np}"
res=requests.get(url)
data=res.json()

    

if inp:
    with st.spinner("searching...."):
     population=data[0]["population"]
    capital=data[0]["capital"][0]
    currency=data[0]["currencies"]
    currency_symbol = list(currency.values())[0]["symbol"]
    currency_name=list(currency.values())[0]["name"]
    flag=data[0]["flag"]
    st.write("• population: "+str(population))
    st.write("• capital: "+capital)
    st.write("• currency: "+ "symbol: " +f":green[{currency_symbol}]"+", name: " +f":green[{currency_name}]")
    st.write("• Flag: "+flag)
    name = data[0]["name"]["common"]
    exists = any(c["country"] == name for c in st.session_state.country)
    if not exists:
            st.session_state.country.insert(
                0,
                {
                    "country": name,
                    "population": population,
                    "capital": capital,
                    "currency symbol": currency_symbol,
                    "currency name": currency_name,
                    "flag": flag,
                },
            )

st.subheader("Previous searches")

for country in st.session_state.country:

    name = country["country"]

    with st.expander(f"{country['flag']} {name}"):
        st.json(country)
