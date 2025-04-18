import streamlit as st
import pandas as pd
import numpy as np 
import joblib

Load the saved similarity matrix

similarity_matrix = joblib.load('food_recommendation_model.pkl')

Sample dish names list (must match the order of similarity_matrix)

dishes = [ "Chole Bhature", "Vada Pav", "Gulab Jamun", "Pesarattu", "Poha", "Pav Bhaji", "Chepala Pulusu", "Kheer", "Aloo Paratha" ]

Streamlit App UI

st.set_page_config(page_title="Food Recommendation System", layout="wide")

wood_bg = """ <style> .stApp { background: url("https://www.transparenttextures.com/patterns/wood-pattern.png"); background-size: cover; color: #3E2723; font-family: 'Segoe UI', sans-serif; } .title h1 { color: #4E342E; text-shadow: 1px 1px #A1887F; } .stButton>button { background-color: #8D6E63; color: white; border-radius: 10px; padding: 0.5em 1em; font-weight: bold; } </style> """ st.markdown(wood_bg, unsafe_allow_html=True)

st.markdown("<div class='title'><h1>Delicious Indian Dish Recommender</h1></div>", unsafe_allow_html=True) st.write("Pick a dish you like, and we’ll suggest similar ones you might enjoy!")

selected_dish = st.selectbox("Choose your favorite Indian dish:", dishes)

def recommend_dishes(selected_dish, similarity_matrix, dishes): index = dishes.index(selected_dish) scores = list(enumerate(similarity_matrix[index])) scores = sorted(scores, key=lambda x: x[1], reverse=True) recommended = [dishes[i] for i, score in scores[1:6]]  # Top 5 recommendations return recommended

if st.button("Recommend Me!"): recommendations = recommend_dishes(selected_dish, similarity_matrix, dishes) st.subheader("Recommended Dishes:") for dish in recommendations: st.success(f"{dish}")
