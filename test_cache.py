import time
import requests

url = "http://localhost:8080/predict"
payload = {
    "text": "WIN a FREE laptop now! Click here: win-now.co/claim"
}

# First request: cache miss
start = time.perf_counter()
response = requests.post(url, json=payload)
miss_time = time.perf_counter() - start

# Next 20 requests: cache hits
hit_times = []

for _ in range(20):
    start = time.perf_counter()
    requests.post(url, json=payload)
    hit_times.append(time.perf_counter() - start)

avg_hit_time = sum(hit_times) / len(hit_times)

print(f"Cache miss: {miss_time * 1000:.3f} ms")
print(f"Average cache hit: {avg_hit_time * 1000:.3f} ms")
print(f"Prediction: {response.json()}")
