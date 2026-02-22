# 🍽️ Swiggy Restaurant Recommendation System

A scalable Restaurant Recommendation System built using Python, Scikit-learn, and Streamlit.  
This project recommends similar restaurants based on cuisine, rating, cost, and city using Cosine Similarity.

---

## 📌 Project Overview

The objective of this project is to build an intelligent restaurant recommendation system using real-world restaurant data.

The system:
- Cleans and preprocesses restaurant data
- Applies One-Hot Encoding on categorical features
- Uses Cosine Similarity for recommendation
- Provides an interactive Streamlit dashboard
- Supports filtering by city, cuisine, rating, and cost

This solution handles large-scale data (148k+ records) using memory-efficient sparse matrix operations.

---

## 🚀 Features

- 🔍 City-based restaurant exploration
- 💖 Similar restaurant recommendation
- 🎯 Filter by:
  - Cuisine
  - Minimum Rating
  - Maximum Cost
- 📊 Top-rated restaurant display
- ⚡ Scalable sparse cosine similarity
- 🎨 Clean, professional Streamlit UI
- 🧠 Memory-efficient implementation

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy (Sparse Matrix)
- Streamlit
- Git & GitHub

---

## 🧠 Recommendation Methodology

### 1️⃣ Data Cleaning
- Removed duplicates
- Handled missing values
- Cleaned rating, cost, and rating_count columns

### 2️⃣ Feature Engineering
- One-Hot Encoding for:
  - City
  - Cuisine
- Numerical features:
  - Rating
  - Rating Count
  - Cost

### 3️⃣ Sparse Matrix Optimization
To handle large data (148k+ rows):
- Used `OneHotEncoder(sparse_output=True)`
- Combined using `scipy.sparse.hstack`
- Converted to CSR format
- Computed cosine similarity on-demand

This avoids creating a massive similarity matrix and keeps memory usage efficient.

### 4️⃣ Recommendation Logic

If user selects:
- Only City → Show top-rated restaurants
- Restaurant → Show similar restaurants within the same city

Filters are applied after similarity computation.

---

## 📊 Business Use Cases

- Personalized restaurant discovery
- Location-based recommendations
- Customer decision support
- Market trend insights
- Food delivery app enhancement

---

📈 **Future Improvements**

-Add search bar with real-time filtering
-Add analytics dashboard (charts & insights)
-Add pagination
-Deploy to Streamlit Cloud
-Add collaborative filtering
