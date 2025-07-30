# Customer Segmentation Project

## Overview
This project performs customer segmentation on the **Online Retail dataset** to group customers into meaningful segments for targeted marketing. It uses **RFM (Recency, Frequency, Monetary) analysis**, **K-Means clustering**, and **DBSCAN clustering**, with **PCA** for visualization. The project includes **time-based analysis** to track customer behavior trends, an **Elbow method** for optimal cluster selection, and enhanced visualizations like boxplots. A **Streamlit dashboard** provides an interactive interface to explore results and export segment assignments.

### Objectives
- **Segment Customers**: Identify groups like Champions (high-value), Potential Loyalists, At-Risk, and New Customers.
- **Analyze Behavior**: Understand customer purchasing patterns for marketing strategies.
- **Visualize Results**: Provide clear, actionable insights through tables and plots.
- **Enable Automation**: Offer modular code for integration or scheduled tasks.

### Target Audience
This project is designed for:
- Data analysts exploring customer behavior.
- Marketing teams targeting customer segments.
- Beginners learning data science with Python, clustering, and visualization.
- Developers integrating segmentation into larger systems.

## Project Structure
```
E:\CustomerSegmentation\
├── notebooks\
│   └── exploratory_analysis.ipynb  # Interactive analysis with Jupyter
├── scripts\
│   ├── app.py                    # Streamlit dashboard
│   ├── segmentation_logic.py     # Modular functions for RFM and clustering
├── data\
│   ├── online_retail.xlsx        # Input dataset
├── assets\
│   ├── cluster_plot.png          # Generated PCA scatter plot
├── requirements.txt              # Dependencies
├── README.md                     # This file
```

## Features
- **Data Cleaning**: Removes invalid entries (e.g., missing `CustomerID`, negative quantities).
- **RFM Analysis**: Calculates Recency (days since last purchase), Frequency (number of purchases), and Monetary (total spend) per customer.
- **Clustering**:
  - **K-Means**: Groups customers into 2–8 clusters (default: 4) with segment names (Champions, Potential Loyalists, At-Risk, New Customers).
  - **DBSCAN**: Identifies outliers and dense clusters.
- **Elbow Method**: Determines optimal number of K-Means clusters.
- **Time-Based Analysis**: Tracks average purchase frequency per month.
- **Visualizations**:
  - PCA scatter plot (saved as `assets/cluster_plot.png`).
  - Boxplots for RFM distribution.
  - Time-based frequency trends.
  - Elbow plot for cluster selection.
- **Streamlit Dashboard**: Interactive interface with cluster parameter adjustments and CSV export.
- **Modular Code**: Functions in `segmentation_logic.py` for reusability.

## Prerequisites
- **Python**: Version 3.10 or higher ([Download](https://www.python.org/downloads/)).
- **Virtual Environment**: To isolate dependencies.
- **Dataset**: `online_retail.xlsx` from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
- **Dependencies**: Listed in `requirements.txt`:
  ```
  pandas==2.2.3
  numpy==2.1.1
  scikit-learn==1.5.2
  matplotlib==3.9.2
  seaborn==0.13.2
  jupyter==1.1.1
  streamlit==1.39.0
  openpyxl==3.1.5
  ```

## Setup Instructions
Follow these steps to set up and run the project on Windows.

### 1. Create Project Directory
- Create the directory structure:
  ```bash
  mkdir E:\CustomerSegmentation
  mkdir E:\CustomerSegmentation\notebooks
  mkdir E:\CustomerSegmentation\scripts
  mkdir E:\CustomerSegmentation\data
  mkdir E:\CustomerSegmentation\assets
  ```
- Place all project files (`exploratory_analysis.ipynb`, `app.py`, `segmentation_logic.py`, `requirements.txt`, `README.md`) in their respective folders as shown in the structure.

### 2. Download Dataset
- Download `online_retail.xlsx` from [UCI](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
- Alternatively, use [Kaggle’s version](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) (`online_retail_II.csv`) and convert to Excel:
  ```python
  import pandas as pd
  df = pd.read_csv('E:/CustomerSegmentation/data/online_retail_II.csv')
  df.to_excel('E:/CustomerSegmentation/data/online_retail.xlsx', index=False)
  ```
- Save the file as `E:\CustomerSegmentation\data\online_retail.xlsx`.
- Verify:
  ```bash
  dir E:\CustomerSegmentation\data
  ```
  - Should list `online_retail.xlsx`.

### 3. Set Up Virtual Environment
- Open Command Prompt or PowerShell (`Win + R`, type `cmd` or `powershell`, press Enter).
- Navigate to project directory:
  ```bash
  cd E:\CustomerSegmentation
  ```
- Create virtual environment:
  ```bash
  python -m venv venv
  ```
  - This creates `E:\CustomerSegmentation\venv\`.
- Activate virtual environment:
  ```bash
  venv\Scripts\activate
  ```
  - Prompt should show `(venv)`.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Verify installations:
  ```bash
  pip list
  ```
  - Ensure all packages from `requirements.txt` are listed.

### 4. Verify File Placement
- Ensure:
  - `exploratory_analysis.ipynb` is in `notebooks/`.
  - `app.py` and `segmentation_logic.py` are in `scripts/`.
  - `requirements.txt` and `README.md` are in `E:\CustomerSegmentation\`.
  - `online_retail.xlsx` is in `data/`.
- Check:
  ```bash
  dir E:\CustomerSegmentation\scripts
  dir E:\CustomerSegmentation\data
  ```

## Running the Project
### Option 1: Jupyter Notebook (`exploratory_analysis.ipynb`)
- **Purpose**: Interactive exploration for data scientists to analyze RFM, clustering, and trends.
- **Run**:
  ```bash
  cd E:\CustomerSegmentation
  venv\Scripts\activate
  jupyter notebook
  ```
  - Open `http://localhost:8888` in your browser.
  - Navigate to `notebooks/exploratory_analysis.ipynb`.
  - Run all cells (Shift + Enter).
- **What It Does**:
  - Loads and cleans `online_retail.xlsx`.
  - Computes RFM features.
  - Applies K-Means (4 clusters) and DBSCAN.
  - Generates Elbow plot for optimal K.
  - Visualizes clusters with PCA, RFM boxplots, and monthly frequency trends.
  - Saves PCA plot to `assets/cluster_plot.png`.

### Option 2: Streamlit Dashboard (`app.py`)
- **Purpose**: Interactive web interface for stakeholders to explore segments and export results.
- **Run**:
  ```bash
  cd E:\CustomerSegmentation
  venv\Scripts\activate
  streamlit run scripts\app.py
  ```
  - Open `http://localhost:8501` in your browser.
- **What It Does**:
  - Provides a dashboard with adjustable parameters:
    - Number of K-Means clusters (2–8, default: 4).
    - Option to use DBSCAN with `eps` (0.1–2.0) and `min_samples` (2–10).
  - Displays Segment Profiles table, PCA scatter plot, boxplots, time-based trends, and Elbow plot.
  - Allows downloading segment assignments as `segment_assignments.csv`.

### Option 3: Segmentation Logic (`segmentation_logic.py`)
- **Purpose**: Contains reusable functions for RFM, clustering, and visualization, used by `app.py` and `exploratory_analysis.ipynb`.
- **Usage**: Not run directly; imported by other components.

## Inputs
- **Dataset**: `E:\CustomerSegmentation\data\online_retail.xlsx`
  - **Source**: UCI Machine Learning Repository.
  - **Columns Used**:
    - `CustomerID`: Unique customer identifier.
    - `InvoiceNo`: Transaction ID (for Frequency).
    - `InvoiceDate`: Purchase date (for Recency).
    - `Quantity`: Items purchased (for Monetary).
    - `UnitPrice`: Price per item (for Monetary).
  - **Cleaning**:
    - Removes rows with missing `CustomerID`.
    - Excludes negative `Quantity` (returns) and zero/negative `UnitPrice`.
    - Converts `InvoiceDate` to datetime.
- **Streamlit Parameters**:
  - Number of K-Means clusters (slider: 2–8).
  - DBSCAN: Enable/disable, `eps` (slider: 0.1–2.0), `min_samples` (slider: 2–10).

## Outputs and Analysis
### 1. Segment Profiles Table
- **Description**: Summarizes mean Recency, Frequency, Monetary, and customer count per cluster.
- **Example**:
  ```
  Cluster  Recency_mean  Recency_count  Frequency_mean  Monetary_mean
  0        10.5         1000           50.2           5000.75
  1        30.2         800            20.1           2000.30
  2        100.7        1200           5.3            500.10
  3        5.1          600            2.0            300.25
  ```
- **Segment Names** (K-Means):
  - Cluster 0: **Champions** (recent, frequent, high spenders).
  - Cluster 1: **Potential Loyalists** (moderate engagement).
  - Cluster 2: **At-Risk** (inactive, low engagement).
  - Cluster 3: **New Customers** (recent, few purchases).
- **DBSCAN**: Clusters labeled as `Cluster X` (X ≥ 0) or `Outlier` (-1).
- **Analysis**:
  - **Champions**: Retain with loyalty programs (e.g., VIP discounts).
  - **Potential Loyalists**: Encourage repeat purchases with promotions.
  - **At-Risk**: Re-engage with “We Miss You” campaigns.
  - **New Customers**: Nurture with welcome emails.
  - **Outliers (DBSCAN)**: Investigate unique behaviors (e.g., high spend, irregular purchases).
- **Business Value**: Prioritize marketing based on segment size and value (e.g., focus on 1200 At-Risk customers to prevent churn).

### 2. PCA Scatter Plot
- **Description**: 2D visualization of customers in PCA space, colored by segment, with point size proportional to Monetary value.
- **Location**: Saved as `E:\CustomerSegmentation\assets\cluster_plot.png`.
- **Analysis**:
  - Well-separated clusters indicate good segmentation.
  - Overlap suggests adjusting cluster parameters.
  - Large points (high Monetary) highlight valuable customers.
- **Business Value**: Validates clustering and communicates segment differences visually.

### 3. Boxplots
- **Description**: Shows distribution of Recency, Frequency, and Monetary per segment.
- **Analysis**:
  - Tight boxes (e.g., low Recency for Champions) indicate consistent behavior.
  - Wide boxes or outliers suggest variability or unique customers.
- **Business Value**: Identifies segment characteristics for tailored strategies.

### 4. Time-Based Trends
- **Description**: Line plot of average purchase frequency per month.
- **Analysis**:
  - Peaks indicate seasonal trends (e.g., holiday shopping).
  - Declines suggest customer churn or reduced engagement.
- **Business Value**: Guides timing for marketing campaigns (e.g., boost promotions during low-frequency months).

### 5. Elbow Plot
- **Description**: Plots K-Means inertia vs. number of clusters (1–9).
- **Analysis**:
  - Choose K where inertia curve flattens (e.g., 4 clusters).
- **Business Value**: Ensures optimal cluster number for meaningful segments.

### 6. CSV Export
- **Description**: `segment_assignments.csv` contains CustomerID, Recency, Frequency, Monetary, and Segment.
- **Example**:
  ```
  CustomerID,Recency,Frequency,Monetary,Segment
  12345,10,50,4500.0,Champions
  12346,25,15,1800.0,Potential Loyalists
  12347,120,3,200.0,At-Risk
  ```
- **Analysis**: Use for personalized marketing (e.g., email campaigns targeting At-Risk customers).
- **Business Value**: Integrates with CRM systems for actionable insights.

## Use Cases
- **Marketing**: Tailor campaigns (e.g., loyalty rewards for Champions, discounts for At-Risk).
- **Customer Retention**: Prevent churn by targeting At-Risk customers.
- **Inventory Management**: Stock products for high-value segments.
- **Automation**: Use `segmentation_logic.py` in scheduled tasks (e.g., Windows Task Scheduler) to update segments.
- **Stakeholder Reporting**: Share interactive results via Streamlit dashboard.
- **Data Science Learning**: Explore RFM, clustering, and visualization techniques.

## Deployment
### Local Deployment
- Run the Streamlit app:
  ```bash
  cd E:\CustomerSegmentation
  venv\Scripts\activate
  streamlit run scripts\app.py
  ```
- Run the notebook:
  ```bash
  jupyter notebook
  ```

### Cloud Deployment
- Push to GitHub:
  ```bash
  cd E:\CustomerSegmentation
  git init
  git add .
  git commit -m "Initial commit"
  git remote add origin <your-repo-url>
  git push origin main
  ```
- Deploy on [Streamlit Community Cloud](https://share.streamlit.io):
  - Sign up, link your GitHub repo, select `app.py`.
  - Include `data/online_retail.xlsx` in the repo or modify `segmentation_logic.py` to fetch it programmatically.

## Troubleshooting
### Import Error
- **Issue**: `app.py` fails with `from scripts.segmentation_logic import *`.
- **Fix**:
  - Ensure `segmentation_logic.py` is in `E:\CustomerSegmentation\scripts\`.
  - Verify directory name (no underscore: `CustomerSegmentation`).
  - Run from correct directory:
    ```bash
    cd E:\CustomerSegmentation
    streamlit run scripts\app.py
    ```
  - Check file existence:
    ```python
    import os
    print(os.path.exists('E:/CustomerSegmentation/scripts/segmentation_logic.py'))
    ```

### FileNotFoundError
- **Issue**: `online_retail.xlsx` not found.
- **Fix**:
  - Ensure file is in `E:\CustomerSegmentation\data\`.
  - Verify path:
    ```python
    import os
    print(os.path.exists('E:/CustomerSegmentation/data/online_retail.xlsx'))
    ```
  - Re-download from [UCI](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).

### Dependency Issues
- **Fix**:
  - Reinstall:
    ```bash
    pip install -r requirements.txt
    ```
  - Verify `openpyxl` for Excel:
    ```bash
    pip show openpyxl
    ```

### Streamlit Issues
- **Issue**: Dashboard doesn’t load at `http://localhost:8501`.
- **Fix**:
  - Check port 8501:
    ```bash
    netstat -a -n -o | find "8501"
    ```
  - Reinstall Streamlit:
    ```bash
    pip install streamlit==1.39.0
    ```

### DBSCAN Output
- **Issue**: Too many outliers (Cluster -1).
- **Fix**: Adjust `eps` or `min_samples` in Streamlit sidebar.

## Citation
- Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.

## Next Steps
- **Extend Analysis**: Add more features (e.g., product category analysis).
- **Automate**: Schedule `segmentation_logic.py` with Windows Task Scheduler.
- **Enhance Dashboard**: Add filters for specific segments or time periods.
- **Contact**: For issues, consult this README or seek help from a data science mentor.
