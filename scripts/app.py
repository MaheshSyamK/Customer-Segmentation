import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
# Add scripts directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from segmentation_logic import *

# Streamlit configuration
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide", initial_sidebar_state="expanded")

# Sidebar
st.sidebar.title("Segmentation Options")
n_clusters = st.sidebar.slider("Number of K-Means Clusters", 2, 8, 4)
use_dbscan = st.sidebar.checkbox("Use DBSCAN Clustering", False)
eps = st.sidebar.slider("DBSCAN eps", 0.1, 2.0, 0.5, 0.1)
min_samples = st.sidebar.slider("DBSCAN min_samples", 2, 10, 5)

# Main content
st.title("Customer Segmentation Dashboard")
st.markdown("Explore customer segments using RFM analysis, K-Means, and DBSCAN clustering on the Online Retail dataset.")

# Load data
@st.cache_data
def load_data():
    return load_and_clean_data()

df = load_data()

# RFM Analysis
rfm = compute_rfm(df)

# Scale and PCA
rfm_scaled, rfm_pca, scaler, pca = scale_and_pca(rfm)

# Clustering
if use_dbscan:
    clusters = dbscan_clustering(rfm_scaled, eps=eps, min_samples=min_samples)
    st.write("Using DBSCAN clustering. Cluster -1 represents outliers.")
else:
    clusters, kmeans = kmeans_clustering(rfm_scaled, n_clusters=n_clusters)

# Segment Profiles
profiles = get_segment_profiles(rfm.copy(), clusters)
st.subheader("Segment Profiles")
st.write(profiles)

# Assign Segment Names (for K-Means only)
if not use_dbscan:
    rfm = assign_segment_names(rfm, clusters)
else:
    rfm['Cluster'] = clusters
    rfm['Segment'] = rfm['Cluster'].apply(lambda x: f"Cluster {x}" if x >= 0 else "Outlier")

# Visualizations
st.subheader("Cluster Visualization")
fig = plot_clusters(rfm_pca, rfm)
st.pyplot(fig)

st.subheader("RFM Distribution")
fig = plot_boxplots(rfm)
st.pyplot(fig)

st.subheader("Time-Based Analysis")
fig = time_based_analysis(df)
st.pyplot(fig)

st.subheader("Elbow Method (K-Means)")
fig = plot_elbow_method(rfm_scaled)
st.pyplot(fig)

# Export Options
st.subheader("Export Results")
if st.button("Download Segment Assignments"):
    rfm[['Recency', 'Frequency', 'Monetary', 'Segment']].to_csv('segment_assignments.csv')
    st.success("Downloaded segment_assignments.csv")
    with open('segment_assignments.csv', 'rb') as f:
        st.download_button("Download Again", f, file_name="segment_assignments.csv")