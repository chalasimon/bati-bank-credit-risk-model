# import pandas as pd
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

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
    def encode_categorical_variables(self,df):
        # Identify categorical columns
        self.df = df
        categorical_cols = ['ProductCategory', 'ProviderId', 'ChannelId']
        
        # One-Hot Encoding for categorical variables
        one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')
        one_hot_encoded = one_hot_encoder.fit_transform(self.df[categorical_cols])
        one_hot_df = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_cols))
        
        # Label Encoding for categorical variables
        label_encoder = LabelEncoder()
        for col in categorical_cols:
            self.df[col] = label_encoder.fit_transform(self.df[col])
        
        # Concatenate the original DataFrame with the one-hot encoded DataFrame
        self.df = pd.concat([self.df, one_hot_df], axis=1)
        
        return self.df
    def handle_missing_values(self, df):
        # Handle missing values by filling with the mean for numerical columns
        numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        for col in numerical_cols:
            df[col].fillna(df[col].mean(), inplace=True)
        
        # Handle missing values by filling with the mode for categorical columns
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        for col in categorical_cols:
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        return df
    
    
        