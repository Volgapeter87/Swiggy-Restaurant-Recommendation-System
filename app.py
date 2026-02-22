# ==========================================
# Swiggy Restaurant Recommendation System
# ==========================================

import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack
from sklearn.preprocessing import OneHotEncoder

# ------------------------------------------
# Page Configuration
# ------------------------------------------

st.set_page_config(
    page_title="Swiggy Recommendation System",
    page_icon="🍽️",
    layout="wide"
)

# ------------------------------------------
# Light Theme CSS
# ------------------------------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fdfbfb, #ebedee);
}
.block-container {
    background: transparent;
}
.title {
    font-size: 38px;
    font-weight: bold;
    color: #6a5acd;
}
.section-title {
    color: #444;
    font-weight: 600;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    border-left: 6px solid #6a5acd;
    transition: 0.3s ease;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.12);
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# Load Data
# ------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_data.csv")

df = load_data()

# ------------------------------------------
# Sidebar Filters
# ------------------------------------------

st.sidebar.title("🔍 Filters")

# City
selected_city = st.sidebar.selectbox(
    "Select City",
    sorted(df['city'].unique())
)

city_df = df[df['city'] == selected_city]

# Restaurant
restaurant_name = st.sidebar.selectbox(
    "Select Restaurant (Optional)",
    ["None"] + list(city_df['name'].unique())
)

# Cuisine Filter
selected_cuisine = st.sidebar.selectbox(
    "Filter by Cuisine",
    ["All"] + sorted(city_df['cuisine'].unique())
)

# Rating Filter
min_rating = st.sidebar.slider(
    "Minimum Rating",
    1.0, 5.0, 3.0, 0.1
)

# Cost Filter
max_cost = st.sidebar.slider(
    "Maximum Cost (₹)",
    int(city_df['cost'].min()),
    int(city_df['cost'].max()),
    int(city_df['cost'].max())
)

# Number of Results
top_n = st.sidebar.slider("Number of Results", 5, 30, 10)

# ------------------------------------------
# Title
# ------------------------------------------

st.markdown('<div class="title">🍽️ Swiggy Restaurant Recommendation System</div>', unsafe_allow_html=True)
st.write("Discover restaurants using AI-powered recommendations ✨")

# ------------------------------------------
# Apply Filters Function
# ------------------------------------------

def apply_filters(data):
    if selected_cuisine != "All":
        data = data[data['cuisine'] == selected_cuisine]
    data = data[data['rating'] >= min_rating]
    data = data[data['cost'] <= max_cost]
    return data

# ------------------------------------------
# CASE 1: Only City Selected
# ------------------------------------------

if restaurant_name == "None":

    st.markdown(f'<div class="section-title">🏆 Restaurants in {selected_city}</div>', unsafe_allow_html=True)

    filtered_df = apply_filters(city_df)

    results = filtered_df.sort_values(
        by=['rating', 'rating_count'],
        ascending=False
    ).head(top_n)

# ------------------------------------------
# CASE 2: Restaurant Selected
# ------------------------------------------

else:

    st.markdown(f'<div class="section-title">💖 Restaurants Similar to {restaurant_name}</div>', unsafe_allow_html=True)

    city_df = city_df.reset_index(drop=True)

    features = city_df[['city', 'cuisine', 'rating', 'rating_count', 'cost']]

    encoder = OneHotEncoder(sparse_output=True, handle_unknown='ignore')
    encoded_categorical = encoder.fit_transform(features[['city', 'cuisine']])

    numerical_data = features[['rating', 'rating_count', 'cost']].values
    city_sparse = hstack([numerical_data, encoded_categorical]).tocsr()

    index = city_df[city_df['name'] == restaurant_name].index[0]

    selected_vector = city_sparse[index:index+1]
    similarity_scores = cosine_similarity(selected_vector, city_sparse).flatten()

    similar_indices = similarity_scores.argsort()[::-1][1:top_n+1]
    similar_restaurants = city_df.iloc[similar_indices]

    results = apply_filters(similar_restaurants)

# ------------------------------------------
# Display Results
# ------------------------------------------

if results.empty:
    st.warning("No restaurants match the selected filters.")
else:
    for _, row in results.iterrows():
        st.markdown(f"""
        <div class="card">
            <h3>{row['name']}</h3>
            📍 {row['address']} <br><br>
            🍜 Cuisine: {row['cuisine']} <br>
            ⭐ Rating: {row['rating']} <br>
            💰 Cost: ₹{int(row['cost'])} <br>
            👥 {int(row['rating_count'])} Ratings
        </div>
        """, unsafe_allow_html=True)
