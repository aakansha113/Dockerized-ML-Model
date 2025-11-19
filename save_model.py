# save_model.py
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import pickle

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200, solver="lbfgs")
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model saved -> model.pkl")

