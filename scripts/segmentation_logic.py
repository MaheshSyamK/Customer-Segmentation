import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

def load_and_clean_data():
    """Load and clean the Online Retail dataset."""
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'online_retail.xlsx')
    df = pd.read_excel(file_path)
    df = df.dropna(subset=['CustomerID'])
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

def compute_rfm(df):
    """Compute RFM features."""
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'count',
        'UnitPrice': lambda x: (x * df.loc[x.index, 'Quantity']).sum()
    }).rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'UnitPrice': 'Monetary'})
    return rfm

def scale_and_pca(rfm, n_components=2):
    """Scale RFM features and apply PCA."""
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)
    pca = PCA(n_components=n_components)
    rfm_pca = pca.fit_transform(rfm_scaled)
    return rfm_scaled, rfm_pca, scaler, pca

def kmeans_clustering(rfm_scaled, n_clusters=4):
    """Apply K-Means clustering."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(rfm_scaled)
    return clusters, kmeans

def dbscan_clustering(rfm_scaled, eps=0.5, min_samples=5):
    """Apply DBSCAN clustering."""
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit_predict(rfm_scaled)
    return clusters

def get_segment_profiles(rfm, clusters):
    """Generate segment profiles."""
    rfm['Cluster'] = clusters
    profiles = rfm.groupby('Cluster').agg({
        'Recency': ['mean', 'count'],
        'Frequency': 'mean',
        'Monetary': 'mean'
    }).round(2)
    return profiles

def assign_segment_names(rfm, clusters):
    """Assign meaningful segment names."""
    rfm['Cluster'] = clusters
    segment_names = {
        0: 'Champions',
        1: 'Potential Loyalists',
        2: 'At-Risk',
        3: 'New Customers'
    }
    rfm['Segment'] = rfm['Cluster'].map(segment_names)
    return rfm

def plot_elbow_method(rfm_scaled):
    """Plot Elbow method for optimal K."""
    inertias = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(rfm_scaled)
        inertias.append(kmeans.inertia_)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range(1, 10), inertias, marker='o')
    ax.set_title('Elbow Method for Optimal K')
    ax.set_xlabel('Number of Clusters')
    ax.set_ylabel('Inertia')
    return fig

def plot_clusters(rfm_pca, rfm, save_path=os.path.join(os.path.dirname(__file__), '..', 'assets', 'cluster_plot.png')):
    """Plot PCA scatter plot."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=rfm_pca[:, 0], y=rfm_pca[:, 1], hue=rfm['Segment'], palette='Set2', size=rfm['Monetary'], sizes=(20, 200), ax=ax)
    ax.set_title('Customer Segments (PCA Reduced)')
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')
    plt.savefig(save_path)
    return fig

def plot_boxplots(rfm):
    """Plot boxplots for RFM features."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for i, feature in enumerate(['Recency', 'Frequency', 'Monetary']):
        sns.boxplot(x='Segment', y=feature, data=rfm, hue='Segment', palette='Set2', ax=axes[i], legend=False)
        axes[i].set_title(f'{feature} Distribution by Segment')
        axes[i].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    return fig

def time_based_analysis(df):
    """Analyze customer frequency trends over months."""
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_freq = df.groupby(['CustomerID', 'Month'])['InvoiceNo'].count().reset_index()
    monthly_trends = monthly_freq.groupby('Month')['InvoiceNo'].mean().reset_index()
    monthly_trends['Month'] = monthly_trends['Month'].astype(str) 
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='Month', y='InvoiceNo', data=monthly_trends, marker='o', ax=ax)
    ax.set_title('Average Customer Frequency Over Time')
    ax.set_xlabel('Month')
    ax.set_ylabel('Average Frequency')
    ax.tick_params(axis='x', rotation=45)
    return fig