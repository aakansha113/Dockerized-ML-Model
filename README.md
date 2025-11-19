# Dockerized ML Model (FastAPI + Docker)

This project demonstrates how to build, containerize, and run a Machine Learning model using FastAPI and Docker.

## 📁 Project Structure

ml-docker-app/
│── model.pkl
│── save_model.py
│── Dockerfile
│── .dockerignore
│── app/
│ ├── main.py
│ ├── requirements.txt

## 1) Create project folder
```
$mkdir ml-docker-app

$cd ml-docker-app
```
## 2) Create virtual environment (optional, for local testing)
```
$python3 -m venv .venv

$source .venv/bin/activate   # on Windows: .venv\Scripts\activate

$pip install --upgrade pip
```
## 3) Write script to train & save a model

Create save_model.py:
# save_model.py 
And then Run:
```
pip install scikit-learn
python save_model.py
```
### (should produce model.pkl)

## 4) Create FastAPI app files

Make folder and files:
```
mkdir app
```
app/main.py

app/requirements.txt

## 5) Test locally (before Docker)

Install requirements and run:
```
$pip install -r app/requirements.txt

$python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open 
### http://127.0.0.1:8000/docs
 and test the /predict endpoint 
 -send e.g. 
 ### { "features": [5.1,3.5,1.4,0.2] }).
