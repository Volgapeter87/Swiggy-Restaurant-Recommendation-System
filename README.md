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
The final solution is deployed using Streamlit with intelligent filter-aware recommendations.

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
✔ Cost Cleaning (₹ removal, conversion)
✔ Rating Count Extraction
✔ One-Hot Encoding (City & Cuisine)
✔ Sparse Matrix Optimization

🤖 Recommendation Models
1️⃣ Cosine Similarity (Final Model)

Computes similarity between selected restaurant and others.
Uses sparse feature matrix.
Fast and scalable.
Provides direct similarity scores.

2️⃣ K-Means Clustering (Compared Model)
Groups restaurants into clusters.
Recommendations generated from same cluster.
Slightly higher intra-cluster similarity.

📊 Model Comparison
Metric	Cosine Similarity	K-Means
Average Similarity Score	0.96+	0.98+
Rating Difference (Lower Better)	Very Low	Higher
Cost Difference (Lower Better)	Lower	Higher
Execution Time	Faster	Slower
✅ Final Model Selected: Cosine Similarity

Reason:
Better rating consistency
Better cost consistency
Faster performance
More interpretable similarity

🧠 Evaluation Strategy

Traditional "accuracy" does not apply to recommendation systems.
Instead, evaluation was done using
Average Cosine Similarity Score
Average Rating Difference
Average Cost Difference
Execution Time Comparison

For production systems, metrics like Precision@K, Recall@K, and NDCG would be used.

🖥 Streamlit Application Logic
Case 1: No Filters Applied

→ Pure cosine similarity on full dataset

Case 2: Filters Applied

→ Dataset restricted based on filters
→ Cosine similarity computed within filtered subset

Filters Available:
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

Activate:
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
✔ GitHub Version Control
✔ Clean Architecture
✔ Production-Ready Structure

🧠 Future Improvements
Precision@K evaluation
User interaction tracking
Hybrid recommendation (Content + Collaborative)
Model deployment on cloud
Similarity score visualization
Real-time API integration

📢 Final Statement

This project demonstrates:
End-to-end ML workflow
Feature engineering & encoding
Clustering & similarity comparison
Evaluation beyond traditional accuracy
Real-world deployment using Streamlit.
