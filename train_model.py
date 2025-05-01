import joblib
from sklearn.ensemble import RandomForestClassifier
from generate_data import generate_synthetic_data
import numpy as np

df = generate_synthetic_data()
X = df.apply(lambda row: row['phq_9_scores'] + row['gad_7_scores'], axis=1).tolist()
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, 'mental_health_model.pkl')
print("Model trained and saved!")
