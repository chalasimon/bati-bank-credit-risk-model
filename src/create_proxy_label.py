#import libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# create_rfm_proxy_target function
# This function creates a proxy target variable based on RFM (Recency, Frequency, Monetary) analysis.
def create_rfm_proxy_target(df: pd.DataFrame, snapshot_date=None):
    df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])

    if snapshot_date is None:
        snapshot_date = df['TransactionStartTime'].max() + pd.Timedelta(days=1)

    rfm_df = df.groupby('CustomerId').agg({
        'TransactionStartTime': lambda x: (snapshot_date - x.max()).days,
        'TransactionId': 'count',
        'Amount': 'sum'
    }).reset_index()
    rfm_df.columns = ['CustomerId', 'Recency', 'Frequency', 'Monetary']

    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_df[['Recency', 'Frequency', 'Monetary']])

    # Apply KMeans clustering to segment customers
    kmeans = KMeans(n_clusters=3, random_state=42)
    rfm_df['Cluster'] = kmeans.fit_predict(rfm_scaled)
    
    # Calculate the mean RFM values for each cluster
    cluster_summary = rfm_df.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean().reset_index()

    # Identify the high-risk cluster
    high_risk_cluster = cluster_summary.sort_values(by=['Recency', 'Frequency', 'Monetary'], ascending=[False, True, True]).iloc[0]['Cluster']
    
    # Create a binary target variable indicating high-risk customers
    rfm_df['is_high_risk'] = (rfm_df['Cluster'] == high_risk_cluster).astype(int)
    return rfm_df[['CustomerId', 'is_high_risk']]
