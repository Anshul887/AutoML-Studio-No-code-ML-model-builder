import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

class AutoMLService:

    def train(self, csv_file, target):

        df = pd.read_csv(csv_file)

        X = df.drop(columns=[target])
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        models = {
            "RandomForest":
                RandomForestClassifier(),

            "LogisticRegression":
                LogisticRegression()
        }

        best_model = None
        best_score = 0

        for name, model in models.items():

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            score = accuracy_score(
                y_test,
                predictions
            )

            if score > best_score:
                best_score = score
                best_model = model

        return {
            "score": best_score,
            "model": best_model
        }
