# AIOps Module 3 — Infrastructure & Containerization

This repository contains my submission for **AIOps Module 3: Infrastructure & Containerization**.

The project implements a CPU-only spam detection API and demonstrates containerization with Docker, caching with Redis, and workload deployment using Kubernetes.

---

## Q1 — Docker Image Optimization

The Q1 implementation compares a single-stage Docker build with a multi-stage Docker build for the spam detection API.

The work includes:

- Creating a single-stage Dockerfile.
- Creating a multi-stage Dockerfile.
- Building and comparing both images.
- Measuring the resulting image sizes.
- Calculating the percentage reduction achieved using the multi-stage build.
- Explaining what remains in the builder stage and what is copied into the final image.

### Files

- `Dockerfile.single` — Single-stage Dockerfile.
- `Dockerfile.multi` — Multi-stage Dockerfile.
- `data/spam_model.joblib` — Trained spam detection model.

---

## Q2 — Docker Compose & Redis Caching

The Q2 implementation extends the spam detection API with Redis-based caching and Docker Compose.

The work includes:

- Checking Redis before running a prediction.
- Storing predictions in Redis on a cache miss.
- Using a 300-second TTL for cached results.
- Returning cached predictions on repeated requests.
- Creating a Docker Compose setup containing the API and Redis.
- Measuring the response time difference between cache miss and cache hit.
- Comparing Docker Compose with Kubernetes.

### Files

- `docker-compose.yml` — API and Redis Compose configuration.
- `test_cache.py` — Cache performance test.
- `app/main.py` — API implementation with Redis caching.
- `requirements.txt` — Python dependencies.

---

## Q3 — Kubernetes Indexed Job

The Q3 implementation uses a Kubernetes Indexed Job to process partitioned user signup data.

The work includes:

- Generating eight deterministic CSV shards.
- Validating exactly one shard per Job completion index.
- Detecting malformed emails and missing required fields.
- Configuring an Indexed Job with `8` completions and `4` parallel pods.
- Using CPU requests and limits for the validation pods.
- Using the Kubernetes Downward API to obtain pod and node information.
- Retrieving completed pod logs through the Kubernetes API.
- Verifying execution across the two-node Minikube cluster.
- Considering how the parallelism could change with three nodes.

### Files

- `q3/generate_shards.py` — Generates the signup data shards.
- `q3/validate_shard.py` — Validates an individual shard.
- `q3/signup_shards/` — Generated CSV shards.
- `q3/signup-validation-job.yaml` — Indexed Job configuration.
- `q3/read_pod_logs.py` — Retrieves validation results through the Kubernetes API.

---

## Q4 — Kubernetes Deployment & Rolling Update

The Q4 implementation deploys the spam detection API using Kubernetes and demonstrates self-healing and rolling updates.

The work includes:

- Creating a Kubernetes Deployment with two replicas.
- Configuring CPU and memory requests and limits.
- Adding a readiness probe using `/healthz`.
- Creating a ClusterIP Service for the API.
- Demonstrating Kubernetes self-healing by deleting a running pod.
- Verifying that the Deployment automatically creates a replacement pod.
- Creating a new API version and image.
- Performing a Kubernetes rolling update.
- Verifying the rollout status and deployment history.
- Comparing a Deployment with a finite Kubernetes Job.

### Files

- `q4/q4-deployment.yaml` — Kubernetes Deployment and Service configuration.
- `app/main.py` — Spam detection API.

---

## Evidence

The `evidence/` folder contains screenshots and supporting evidence for Q1, Q2, Q3 and Q4.

The final written submission is:

- `AIOps_A2_report.pdf` — Final assignment report.

---

## Repository Structure

```text
AIOps_A2/
│
├── app/
│   └── main.py
│
├── data/
│   ├── spam_dataset.csv
│   └── spam_model.joblib
│
├── q3/
│   ├── signup_shards/
│   ├── generate_shards.py
│   ├── validate_shard.py
│   ├── signup-validation-job.yaml
│   └── read_pod_logs.py
│
├── q4/
│   └── q4-deployment.yaml
│
├── evidence/
│   └── ...
│
├── Dockerfile.single
├── Dockerfile.multi
├── docker-compose.yml
├── generate_dataset.py
├── train_model.py
├── test_cache.py
├── requirements.txt
├── AIOps_A2_report.pdf
└── README.md
