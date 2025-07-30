Customer Segmentation Project
Overview
This project performs customer segmentation on the Online Retail dataset (online_retail.xlsx) using RFM (Recency, Frequency, Monetary) analysis, K-Means, and DBSCAN clustering, with PCA for visualization. It includes time-based analysis, optimal cluster determination, and an interactive Streamlit dashboard.
Features

Data cleaning and preprocessing
RFM feature engineering
Optimal K determination via Elbow method
K-Means and DBSCAN clustering
Time-based frequency analysis
Visualizations: scatter plots, boxplots, time trends, Elbow plot
Streamlit dashboard with export options

Project Structure
CustomerSegmentation/
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   ├── app.py
│   ├── segmentation_logic.py
├── data/
│   └── online_retail.xlsx
├── assets/
│   └── cluster_plot.png
├── requirements.txt
├── README.md

Prerequisites

Python 3.10+ (Download)
Virtual environment
Dependencies in requirements.txt
Dataset: online_retail.xlsx in data/

Setup

Create Directory:
Set up E:\CustomerSegmentation with the structure above.


Download Dataset:
Get online_retail.xlsx from UCI.
Place in E:\CustomerSegmentation\data\.


Create Virtual Environment:cd E:\CustomerSegmentation
python -m venv venv
venv\Scripts\activate


Install Dependencies:pip install -r requirements.txt



Running the Project
1. Exploratory Analysis (exploratory_analysis.ipynb)

Purpose: Interactive exploration with Elbow method, DBSCAN, and time-based analysis.
Run:jupyter notebook


Open notebooks/exploratory_analysis.ipynb and run all cells.


Outputs:
Segment Profiles table
PCA scatter plot (assets/cluster_plot.png)
Boxplots for RFM features
Time-based frequency trends
Elbow plot



2. Streamlit Dashboard (app.py)

Purpose: Interactive visualization with clustering options and export.
Run:streamlit run scripts\app.py


Open http://localhost:8501.


Outputs:
Segment Profiles table
PCA scatter plot
Boxplots
Time-based trends
Elbow plot
Downloadable segment assignments



3. Segmentation Logic (segmentation_logic.py)

Purpose: Modular functions for RFM, clustering, and visualization.

Inputs

Dataset: online_retail.xlsx in data/.
Columns: CustomerID, InvoiceNo, InvoiceDate, Quantity, UnitPrice, etc.
Cleaned: Removes missing CustomerID, negative Quantity, zero/negative UnitPrice.


Parameters (Streamlit):
Number of K-Means clusters (2–8)
DBSCAN parameters (eps, min_samples)



Outputs and Analysis

Segment Profiles Table:
Example:Cluster  Recency_mean  Recency_count  Frequency_mean  Monetary_mean
0        10.5         1000           50.2           5000.75
1        30.2         800            20.1           2000.30
2        100.7        1200           5.3            500.10
3        5.1          600            2.0            300.25


Analysis: Prioritize Champions (high value); re-engage At-Risk customers.


PCA Scatter Plot:
Saved as assets/cluster_plot.png.
Analysis: Confirms cluster separation; outliers indicate unique behaviors.


Boxplots:
Shows RFM distribution per segment.
Analysis: Identifies variability (e.g., Champions have tight Recency).


Time-Based Trends:
Plots average frequency per month.
Analysis: Detects seasonal patterns or declining engagement.


Elbow Plot:
Guides optimal K selection.
Analysis: Choose K where inertia flattens (e.g., 4).


CSV Export:
segment_assignments.csv with RFM and segment assignments.



Deployment

Local: Run streamlit run scripts\app.py.
Cloud:git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push origin main


Deploy via Streamlit Community Cloud, selecting app.py.
Include data/online_retail.xlsx in the repo or modify code to fetch it.



Troubleshooting

Import Error:
Ensure segmentation_logic.py is in E:\CustomerSegmentation\scripts\.
Verify directory name: E:\CustomerSegmentation (no underscore).
Check working directory:cd E:\CustomerSegmentation
streamlit run scripts\app.py




FileNotFoundError:
Ensure online_retail.xlsx is in E:\CustomerSegmentation\data\.
Run:import os
print(os.path.exists('E:/CustomerSegmentation/data/online_retail.xlsx'))


Re-download from UCI.


Dependencies:
Reinstall: pip install -r requirements.txt.
Verify openpyxl: pip show openpyxl.


Streamlit: Check port 8501 and streamlit==1.39.0.

Citation

Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.
