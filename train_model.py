import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("data/spam_dataset.csv")

# Features and labels
X = df["text"]
y = df["label"]

# TF-IDF + Multinomial Naive Bayes
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train
model.fit(X, y)

# Save trained model
joblib.dump(model, "data/spam_model.joblib")

print("Model trained successfully.")
print(f"Training samples: {len(df)}")
print("Model saved to data/spam_model.joblib")
