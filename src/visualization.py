# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_numerical_distribution(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_categorical_distribution(self, column):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.data, x=column)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.show()
    def plot_correlation_matrix(self):
        plt.figure(figsize=(12, 8))
        correlation_matrix = self.data.corr()
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