# 🚀 Kubernetes Deployment of a Microservice on AWS EC2

A cloud-native microservice built with FastAPI, containerized using Docker, and deployed on Kubernetes running on AWS EC2 infrastructure.  
This project demonstrates real-world DevOps workflows including local testing, cloud deployment, and service exposure.

---

## 📌 Project Overview

This project showcases a complete DevOps lifecycle for a microservice:

- Local development and testing using Docker
- Containerization with a production-ready Dockerfile
- Deployment and orchestration using Kubernetes
- Cloud hosting on AWS EC2 (t3.small instance)
- External access via Kubernetes Service (NodePort)

The focus is on **scalability, availability, and real-world cloud deployment practices**.

---

## 🛠️ Tech Stack

🧩 **Backend:** FastAPI (Python)  
🐳 **Containerization:** Docker  
☸️ **Orchestration:** Kubernetes  
☁️ **Cloud Platform:** AWS EC2 (t3.small)  
🖥️ **Tools:** Docker CLI, kubectl  

---

## 📂 Project Structure

```
k8s-microservice/
├── app/
│   ├── main.py
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── README.md
└── .gitignore
```

---

## ⚙️ Application Details

The backend microservice is built using **FastAPI** and returns JSON-based responses.

### 🔗 API Endpoints

- **GET /** → Service health check  
- **GET /info** → Application metadata  

### 📦 Sample Response
```json
{
  "service": "K8s Microservice",
  "status": "RUNNING"
}
```

---

## 🐳 Docker Implementation (Local Verification)

Before deploying to Kubernetes, the application is tested locally using Docker.

### 🔨 Build Docker Image
```bash
docker build -t k8s-microservice:1.0 .
```

### ▶️ Run Container
```bash
docker run -d -p 8000:8000 k8s-microservice:1.0
```

🌐 Access locally at:
```
http://localhost:8000
```

📌 This step ensures the containerized application works correctly before cloud deployment.

---

## ☸️ Kubernetes Deployment on AWS EC2

### 🖥️ Cloud Infrastructure (AWS)

- Launched an **AWS EC2 instance (t3.small)**  
- Installed Docker and Kubernetes tooling on EC2  
- Used EC2 as the Kubernetes node for deployment  
- Selected t3.small to meet Kubernetes memory requirements  

> The EC2 instance was later terminated to optimize cost after successful deployment and testing.

---

### 📦 Kubernetes Deployment

- Used a **Kubernetes Deployment** to manage application pods  
- Configured **multiple replicas** for high availability  
- Kubernetes handles pod restarts automatically  

---

### 🌐 Kubernetes Service

- Exposed the application using a **NodePort Service**
- Enabled external access via EC2 public IP and node port

### 🚀 Apply Kubernetes Manifests
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

🌍 Application accessible at:
```
http://<EC2_PUBLIC_IP>:<NODE_PORT>
```

---

## ✨ Key Features

✅ Dockerized microservice architecture  
✅ Kubernetes-based orchestration  
✅ Cloud deployment using AWS EC2  
✅ Replica-based scalability  
✅ External service exposure  

---

## 🏭 Real-World Use Case

This architecture is commonly used in:
- SaaS backend platforms
- E-commerce microservices
- FinTech and enterprise systems
- Cloud-native applications requiring scalability and reliability

---

## 🔮 Future Enhancements

📈 Horizontal Pod Autoscaling (HPA)  
🌐 Ingress Controller  
🔁 CI/CD pipeline integration  
📊 Monitoring and logging  

---

## 👤 Author

**Vaibhav Sudrik**  
Email: vaibhavsudrik2005@gmail.com
Cloud Computing & DevOps Enthusiast  
📍 Maharashtra, India
