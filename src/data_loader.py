# import libraries
import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        """
        Initialize the DataLoader with the path to the CSV file.
        
        :param file_path: Path to the CSV file containing the dataset.
        """
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """
        Load the dataset from the specified CSV file.
        
        :return: A pandas DataFrame containing the dataset.
        """
        try:
            data = pd.read_csv(self.file_path)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()