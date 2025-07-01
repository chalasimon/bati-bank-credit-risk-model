# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_numerical_distribution(self, column):
        fig, axes = plt.subplots(2, len(column), figsize=(15, 8)) 
        fig.tight_layout(pad=5.0) 
        # Histograms with KDE
        for i, col in enumerate(column):
            sns.histplot(self.data[col], kde=True, bins=30, ax=axes[0, i])
            axes[0, i].set_title(f'Distribution of {col}')
            axes[0, i].set_xlabel(col)
            axes[0, i].set_ylabel('Frequency')
        # Boxplots
        for i, col in enumerate(column):
            sns.boxplot(x=self.data[col], ax=axes[1, i])
            axes[1, i].set_title(f'Boxplot of {col}')
            axes[1, i].set_xlabel(col)
        plt.show()

    def plot_categorical_distribution(self, columns):
        n_cols = len(columns)
        # Calculate grid dimensions - 2 rows, enough columns to fit all plots
        n_rows = 2
        n_plot_cols = (n_cols + 1) // 2  # Round up
        
        fig, axes = plt.subplots(n_rows, n_plot_cols, figsize=(15, 10))
        fig.tight_layout(pad=5.0)
        
        # Flatten axes array for easier indexing
        axes = axes.flatten()
        
        for i, col in enumerate(columns):
            sns.countplot(data=self.data, x=col, ax=axes[i])
            axes[i].set_title(f'Distribution of {col}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel('Count')
            axes[i].tick_params(axis='x', rotation=45)
        
        # Hide any unused axes
        for j in range(i+1, len(axes)):
            axes[j].set_visible(False)
        
        plt.tight_layout()
        plt.show()
    def plot_correlation_matrix(self, columns=None):
        plt.figure(figsize=(12, 8))
        if columns is None:
            columns = self.data.select_dtypes(include=['number']).columns
        correlation_matrix = self.data[columns].corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
        plt.title('Correlation Matrix')
        plt.show()
    def correlation_heatmap(self, columns=None):
            plt.figure(figsize=(12, 8))
            if columns is None:
                columns = self.data.select_dtypes(include=['number']).columns
            correlation_matrix = self.data[columns].corr()
            sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
            plt.title('Correlation Heatmap')
            plt.show()
    def analyze_missing_values(self):
        data = self.data
        # Identifying missing values in each column
        if data.isnull().sum().sum() == 0:
            print("No missing values found in the dataset.")
            return
        
        missing_values = data.isnull().sum()
        missing_values = missing_values[missing_values > 0]
        # Visualizing missing values
        plt.figure(figsize=(12, 6))
        sns.barplot(x=missing_values.index, y=missing_values.values)
        plt.title('Missing Values Count')
        plt.xticks(rotation=45)
        plt.show()