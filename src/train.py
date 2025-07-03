import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from src.model_utils import evaluate_model, log_model_with_mlflow

class CR_Trainer:
    def __init__(self, data: pd.DataFrame):
        self.df = data
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.models = {
            "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
            "RandomForest": RandomForestClassifier(random_state=42)
        }

    def preprocess(self):
        self.X = self.df.drop(columns=['is_high_risk', 'CustomerId'], errors='ignore')
        self.y = self.df['is_high_risk']
        self.X = pd.get_dummies(self.X, drop_first=True)

    def split_data(self, test_size=0.2, random_state=42):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, stratify=self.y, random_state=random_state
        )

    def train_and_evaluate(self):
        for name, model in self.models.items():
            model.fit(self.X_train, self.y_train)
            metrics = evaluate_model(model, self.X_test, self.y_test)
            print(f"{name} Metrics:", metrics)
            log_model_with_mlflow(model, name, metrics)

    def run_pipeline(self):
        self.preprocess()
        self.split_data()
        self.train_and_evaluate()
