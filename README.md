🍽 Swiggy Restaurant Recommendation System
📌 Project Overview

This project builds a Content-Based Restaurant Recommendation System using restaurant metadata such as:

City

Cuisine

Rating

Rating Count

Cost

The system recommends similar restaurants using:

✅ Cosine Similarity (Final Model)

✅ K-Means Clustering (Compared Model)

The final application is deployed using Streamlit with intelligent filter-aware recommendations.

🎯 Business Objective

To help users discover restaurants similar to their preferences while allowing optional refinement filters for:

City

Cuisine

Rating

Cost

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-Learn

SciPy

Streamlit

Git & GitHub

📂 Project Structure
swiggy_recommendation/
│
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── models/
│   └── encoder.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_model_comparison.ipynb
│
├── app.py
├── requirements.txt
└── README.md
🔄 Project Workflow

Data Cleaning

Feature Engineering

One-Hot Encoding

Sparse Matrix Creation

Model Building (Cosine & KMeans)

Model Comparison

Streamlit Deployment

🧹 Data Preprocessing

✔ Duplicate Removal

✔ Missing Value Handling

✔ Rating Conversion to Numeric

✔ Cost Cleaning (₹ removal and numeric conversion)

✔ Rating Count Extraction

✔ One-Hot Encoding (City & Cuisine)

✔ Sparse Matrix Optimization

🤖 Recommendation Models
1️⃣ Cosine Similarity (Final Model)

Computes similarity between selected restaurant and others

Uses sparse feature matrix

Fast and scalable

Provides direct similarity scores

2️⃣ K-Means Clustering (Compared Model)

Groups restaurants into clusters

Recommendations generated from same cluster

Used for model comparison

📊 Model Comparison
Metric	Cosine Similarity	K-Means
Average Similarity Score	0.96+	0.98+
Rating Difference (Lower Better)	Lower	Higher
Cost Difference (Lower Better)	Lower	Higher
Execution Time	Faster	Slower
✅ Final Model Selected: Cosine Similarity

Reason:

Better rating consistency

Better cost consistency

Faster performance

More interpretable similarity results

🧠 Evaluation Strategy

Traditional “accuracy” does not apply to recommendation systems.

Instead, evaluation was performed using:

Average Cosine Similarity Score

Average Rating Difference

Average Cost Difference

Execution Time Comparison

In production systems, additional metrics like Precision@K, Recall@K, and NDCG can be used.

🖥 Streamlit Application Logic
Case 1: No Filters Applied

→ Pure cosine similarity on full dataset

Case 2: Filters Applied

→ Dataset restricted based on filters
→ Cosine similarity computed within filtered subset

Available Filters

Number of Recommendations (5–30)

Minimum Rating

Maximum Cost

City

Cuisine

This ensures:

Intelligent recommendations

Location-aware suggestions

Filter-aware similarity

🚀 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/Volgapeter87/Swiggy-Restaurant-Recommendation-System.git
cd Swiggy-Restaurant-Recommendation-System
2️⃣ Create Virtual Environment
python -m venv venv

Activate (Windows):

venv\Scripts\activate
3️⃣ Install Requirements
pip install -r requirements.txt
4️⃣ Run Streamlit App
streamlit run app.py
📌 Key Features

✔ Content-Based Recommendation

✔ Memory Efficient Sparse Matrix

✔ Model Comparison (Cosine vs KMeans)

✔ Intelligent Filter-Aware Logic

✔ Clean Architecture

✔ Production-Ready Structure

🔮 Future Improvements

Precision@K evaluation

Hybrid Recommendation (Content + Collaborative)

Cloud Deployment

Real-time API integration

Similarity score visualization

📢 Final Note

This project demonstrates:

End-to-end Machine Learning workflow

Feature engineering & encoding

Clustering & similarity comparison

Evaluation beyond traditional accuracy

Real-world deployment using Streamlit
