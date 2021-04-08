from joblib import dump
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


if __name__ == "__main__":

    # Read data and drop categorical feature for this exercise
    features = pd.read_csv("data.csv")
    features = features.drop("week", axis=1)

    labels = np.array(features["actual"])
    features = features.drop("actual", axis=1)

    feature_list = list(features.columns)
    features = np.array(features)

    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.25
    )

    baseline_preds = X_test[:, feature_list.index("average")]
    baseline_errors = abs(baseline_preds - y_test)

    rf = RandomForestRegressor(n_estimators=1000)
    rf.fit(X_train, y_train)

    predictions = rf.predict(X_test)
    errors = abs(predictions - y_test)

    print(f"Average baseline error:  {round(np.mean(baseline_errors), 2)} degrees.")
    print(f"Mean Absolute Error: {round(np.mean(errors), 2)}, degrees.")

    dump(rf, "model.joblib")
