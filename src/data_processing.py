# import pandas as pd
import pandas as pd
import numpy as np

class FeatureEngineering:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def remove_duplicates(self):
        # Remove duplicate rows from the DataFrame
        initial_shape = self.df.shape
        self.df.drop_duplicates(inplace=True)
        final_shape = self.df.shape
        print(f"Removed {initial_shape[0] - final_shape[0]} duplicate rows.")
        return self.df
    def create_aggregated_features(self):
        # aggregated features of Total Transaction Amount: Sum of all transaction amounts for each customer.
        self.df['total_transaction_amount'] = self.df['Amount'].sum()
        # aggregated features of Average Transaction Amount: Average transaction amount per customer.
        self.df['average_transaction_amount'] = self.df['Amount'].mean()
        # aggregated features of Transaction Count: Number of transactions per customer
        self.df['transaction_count'] = self.df['Amount'].count()
        # aggregated features of Standard Deviation of Transaction Amounts: Variability of transaction amounts per customer
        self.df['std_transaction_amount'] = self.df['Amount'].std()
        return self.df
    def extract_time_features(self):
        # Extract time features from the 'TransactionTime' column
        self.df['TransactionStartTime'] = pd.to_datetime(self.df['TransactionStartTime'], errors='coerce')
        self.df['TransactionHour'] = self.df['TransactionStartTime'].dt.hour
        self.df['TransactionDay'] = self.df['TransactionStartTime'].dt.day
        self.df['TransactionMonth'] = self.df['TransactionStartTime'].dt.month
        self.df['TransactionYear'] = self.df['TransactionStartTime'].dt.year
        return self.df
    
    
        