# ==========================================
# Swiggy Restaurant Recommendation System
# ==========================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack

# ==========================================
# 1. Load Data
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_data.csv")

df = load_data()

# ==========================================
# 2. Load Encoder
# ==========================================

@st.cache_resource
def load_encoder():
    with open("models/encoder.pkl", "rb") as f:
        return pickle.load(f)

encoder = load_encoder()

# ==========================================
# 3. Prepare Feature Matrix
# ==========================================

def prepare_features(data):

    features = data[['city', 'cuisine', 'rating', 'rating_count', 'cost']]

    encoded_categorical = encoder.transform(features[['city', 'cuisine']])

    numerical_data = features[['rating', 'rating_count', 'cost']].values

    return hstack([numerical_data, encoded_categorical]).tocsr()

feature_matrix = prepare_features(df)

# ==========================================
# 4. Cosine Recommendation Function
# ==========================================

def recommend_cosine(index, data, top_n=10):

    selected_vector = data[index:index+1]

    similarity_scores = cosine_similarity(selected_vector, data).flatten()

    similar_indices = similarity_scores.argsort()[::-1][1:top_n+1]

    return similar_indices

# ==========================================
# 5. Streamlit UI
# ==========================================

st.title("🍽 Swiggy Restaurant Recommendation System")
st.write("Select a restaurant to get personalized recommendations.")

restaurant_list = df['name'].values
selected_restaurant = st.selectbox("Choose a Restaurant", restaurant_list)

# ==========================================
# Sidebar Filters (Refinement Only)
# ==========================================

st.sidebar.header("Refine Recommendations")

top_n = st.sidebar.slider("Number of Recommendations", 5, 30, 10)

min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 0.0)

max_cost = st.sidebar.number_input(
    "Maximum Cost",
    min_value=0,
    value=int(df['cost'].max())
)

city_options = ["All"] + sorted(df['city'].unique().tolist())
selected_city = st.sidebar.selectbox("City", city_options)

cuisine_options = ["All"] + sorted(df['cuisine'].unique().tolist())
selected_cuisine = st.sidebar.selectbox("Cuisine", cuisine_options)

sort_option = st.sidebar.selectbox(
    "Sort By",
    ["None", "Rating (High to Low)", "Cost (Low to High)"]
)

# ==========================================
# Generate Recommendations
# ==========================================

if st.button("Get Recommendations"):

    selected_index = df[df['name'] == selected_restaurant].index[0]

    recommended_indices = recommend_cosine(
        selected_index,
        feature_matrix,
        top_n=top_n
    )

    recommendations = df.iloc[recommended_indices]

    # Apply filters
    recommendations = recommendations[
        (recommendations['rating'] >= min_rating) &
        (recommendations['cost'] <= max_cost)
    ]

    if selected_city != "All":
        recommendations = recommendations[
            recommendations['city'] == selected_city
        ]

    if selected_cuisine != "All":
        recommendations = recommendations[
            recommendations['cuisine'] == selected_cuisine
        ]

    if sort_option == "Rating (High to Low)":
        recommendations = recommendations.sort_values(
            by="rating", ascending=False
        )

    elif sort_option == "Cost (Low to High)":
        recommendations = recommendations.sort_values(
            by="cost", ascending=True
        )

    st.subheader("Recommended Restaurants")

    if recommendations.empty:
        st.warning("No restaurants found with selected filters.")
    else:
        for _, row in recommendations.iterrows():
            st.markdown(f"""
            **{row['name']}**  
            📍 {row['city']}  
            🍜 {row['cuisine']}  
            ⭐ Rating: {row['rating']}  
            💰 Cost: ₹{row['cost']}  
            ---
            """)