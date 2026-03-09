import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, f1_score

import config

print("Loading dataset...")

# Load dataset
df = pd.read_csv(config.DATA_PATH)

# Remove unwanted columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Features and labels
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("Training models...")

models = {
    "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
    "Decision Tree": DecisionTreeClassifier(),
    "Naive Bayes": GaussianNB()
}

results = []

best_model = None
best_accuracy = 0

for name, model in models.items():

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average="weighted")

    results.append({
        "Model": name,
        "Key Settings": str(model),
        "Accuracy": round(acc, 4),
        "F1 Score": round(f1, 4)
    })

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model

# Save results table
results_df = pd.DataFrame(results)

results_df.to_csv("data/model_results.csv", index=False)

# Save best model
joblib.dump(best_model, config.MODEL_PATH)

# Save symptoms list
joblib.dump(X.columns.tolist(), config.SYMPTOMS_PATH)

# Save test data for analytics
joblib.dump(X_test, "data/X_test.pkl")
joblib.dump(y_test, "data/y_test.pkl")

print("Training complete!")
print("\nModel Comparison Results:\n")
print(results_df)