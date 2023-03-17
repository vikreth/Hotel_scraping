import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    image = Image.open('itc.png')
    st.image(image, caption='Institute of Technology of Cambodia')

with col3:
    st.write(' ')


st.markdown("<h1 style='text-align: center; color: red;'>Hotel Scraping</h1>", unsafe_allow_html=True)

tag = st.selectbox('choose a topic', [
                   'phnom-penh', 'siemreab', 'kampong-saom', 'kampot', 'koh-rong-island', 'kep', 'kracheh'])

generate = st.button('Generate csv')

url = f"https://www.booking.com/city/kh/{tag}.en-gb.html?aid=356980&label=gog235jc-1FCAIoeEICa2hIM1gDaHiIAQGYAQm4ARfIAQzYAQHoAQH4AQ2IAgGoAgO4ArjCz6AGwAIB0gIkMjIwYWRkMGUtNzFjYy00YWQ0LWJjYTctY2U5OTQxNjUwODVl2AIG4AIB&sid=44bbee00a2786e82638be4a5e5dfa113&inac=0&changed_currency=1&selected_currency=USD&top_currency=1"

res = requests.get(url)

content = BeautifulSoup(res.content, 'html.parser')

quotes = content.find_all('div', class_='sr__card js-sr-card')

file = []

for quote in quotes:
    des = quote.find('p', class_='bui-card__text hotel-card__text--wrapped bui-spacer--small').text
    name = quote.find('span', class_='bui-card__title').text
    rate = quote.find('div', class_='bui-review-score__badge').text
    loca = quote.find('span', itemprop = 'addressLocality').text
    price = quote.find(
        'div', class_='bui-price-display__value bui-f-color-constructive').text
    link = quote.find('a')
    st.success(name)
    st.success(des)
    st.success(price)
    st.success(rate)
    st.success(loca)

    st.markdown(
        f"<a href=https://www.booking.com{link['href']}>{name} </a>", unsafe_allow_html=True)
    file.append([name, rate, price,  link])

if generate:
    try:
        df = pd.DataFrame(file)
        df.to_csv('Hotel.csv', index=False, header=[
                  'description', 'Name', 'Rate', 'Price', 'Link'], encoding='cp1252')

    except:
        st.write('Loading...')

st.markdown("""---""")
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    image = Image.open('Untitled-5.png')
    st.image(image, caption='OUN VIKRETH')

with col2:
    image = Image.open('Untitled-1.png')
    st.image(image, caption='PHENG SOTHEA')

with col3:
    image = Image.open('Untitled-6.png')
    st.image(image, caption='NGIM PANHA')

with col4:
    image = Image.open('Untitled-2.png')
    st.image(image, caption='NANG SREYNICH')
    
with col5:
    image = Image.open('Untitled-3.png')
    st.image(image, caption='MAO KIMLANG')

with col6:
    image = Image.open('Untitled-4.png')
    st.image(image, caption='PEAN CHINGER')
