import streamlit as st
# import requests
import pandas as pd
import pickle

# ============= DATA LOADING =============

with open("pipe_linear_regression.pkl", "rb") as model_file:
    model = pickle.load(model_file)

df = pd.read_csv('house_price_pred.csv')
mask_floors = {1: 1, 1.5 : 1, 2:2, 2.5:2, 3:3, 3.5:3}
df['floors'] = df['floors'].map(mask_floors)
df['yr_renovated'] = df['yr_renovated'].apply(lambda x: 0 if x==0 else 1)
# price = df['price']

st.title("Aplikasi Prediksi Harga Rumah di Negara Amerika Serikat (USA)")
st.write("Created by Lutfi Adam")

columns = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'condition', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated',
       'city']

# ============= INPUT =============
city = st.selectbox("Lokasi Kota", df['city'].unique())
bedroom = st.selectbox("Kamar Tidur", df['bedrooms'].unique())
bathroom = st.selectbox("Kamar Mandi", df['bathrooms'].unique())
floor = st.selectbox("Tingkatan Rumah", df['floors'].unique())
condition = st.selectbox("Kondisi Rumah", df['condition'].unique())
above = st.number_input("Luas Tanah")
lot = st.number_input("Luas Halaman Rumah")
living = st.number_input("Luas Ruang Tamu")
basement = st.number_input("Luas Ruang Bawah Tanah")
year_build = st.number_input('Tahun Rumah dibangun')
renovated = st.selectbox("Rumah Sudah di Renovasi (Sudah direnovasi = 1, Belum direnovasi = 0)", df['yr_renovated'].unique())



# =========== INFERENCE =============
new_data = [bedroom,bathroom,living,lot,floor,condition,above,basement,year_build,renovated,city]
new_data = pd.DataFrame([new_data], columns=columns)
res = model.predict(new_data)
press = st.button('PREDIKSI')
if press:
    st.write(f'HARGA RUMAH : {res[0]}')