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

## Step-by-step Procedure:
### 1) Create project folder
```
mkdir ml-docker-app

cd ml-docker-app
```
### 2) Create virtual environment (optional, for local testing)
```
python3 -m venv .venv

source .venv/bin/activate   # on Windows: .venv\Scripts\activate

pip install --upgrade pip
```
### 3) Write script to train & save a model

Create save_model.py:
#### save_model.py 
And then Run:
```
pip install scikit-learn
python save_model.py
```
### (should produce model.pkl)

### 4) Create FastAPI app files

Make folder and files:
```
mkdir app
```
app/main.py

app/requirements.txt

### 5) Test locally (before Docker)

Install requirements and run:
```
pip install -r app/requirements.txt

python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```
Open 
```
http://127.0.0.1:8000/docs
```
and test the /predict endpoint 
send e.g. 
#### { "features": [5.1,3.5,1.4,0.2] }).

### 6) Add .dockerignore
Create .dockerignore to keep image small:

### 7) Create Dockerfile (multi-stage, small final size)
Dockerfile

#### Notes:
1- Uses python:3.10-slim to avoid the "Requires-Python >=3.10" pip issue.

2- --workers 1 is safe for CPU-bound models; increase or use Gunicorn + Uvicorn worker for production.

###                OR

### 📥 Clone This Repository
#### To clone this portfolio on your local system, run:
```
git clone https://github.com/aakansha113/Dockerized-ML-Model.git
```
### 8) Build Docker image

From project root:
```
docker build -t ml-model:latest .
```
If you see pip errors about Python version, make sure Dockerfile base image is python:3.10-slim
### 9) Run container locally
```
docker run --rm -p 8000:8000 --name ml-local ml-model:latest
```
Open 
```
 http://localhost:8000/docs
```
in browser to use Swagger UI.

## 🔧 Production Tips
- Use a process manager (systemd, docker-compose, or Kubernetes) to auto-restart containers.
  
- For concurrency in production, use Gunicorn with Uvicorn workers:
```
gunicorn -k uvicorn.workers.UvicornWorker -w 4 app.main:app
```
- Serve model files from a mounted volume or object storage (e.g., AWS S3) if models update frequently.
  
- Add logging using Python's `logging` module. Ensure logs go to stdout (Docker captures stdout).
  
- Secure endpoints before exposing publicly (API keys, tokens, OAuth).


## 🛠 Troubleshooting
- **Ignored Python versions**: Use Docker base image `python:3.10` or higher.
  
- **Model not found**: Ensure
```
COPY model.pkl /app/model.pkl
```
and rebuild the image.

- **Container exits after starting**: Check logs:
```
docker logs <container-id>
```
- **Port already in use**: Change port mapping:
```
docker run -p 8080:8000 ml-model:latest
```


## ✅ Pre‑Deployment Checklist
- `python save_model.py` → `model.pkl` must exist.
  
- Local test:
  ```
  python -m uvicorn app.main:app --reload
  ```
  
- Docker image builds:
  ```
  docker build -t ml-model:latest .
  ```
- API responds in container:
  ```
  docker run -p 8000:8000 ml-model:latest
  ```
- Add healthcheck & restart policy before production deployment.

### ⭐ Show Your Support
#### If you like this portfolio, feel free to ⭐ star the repo!
