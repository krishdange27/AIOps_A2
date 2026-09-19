import csv
import random
from pathlib import Path

random.seed(42)

output_dir = Path("signup_shards")
output_dir.mkdir(exist_ok=True)

names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rahul",
    "Rohan", "Neha", "Priya", "Ananya", "Kavya"
]

for shard in range(8):
    rows = []

    for i in range(20):
        user_id = shard * 20 + i + 1
        name = random.choice(names)
        email = f"user{user_id}@example.com"

        # Add deterministic malformed records
        if i == 5:
            email = f"user{user_id}example.com"

        if i == 12:
            name = ""

        rows.append({
            "user_id": user_id,
            "name": name,
            "email": email
        })

    with open(output_dir / f"shard_{shard}.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["user_id", "name", "email"])
        writer.writeheader()
        writer.writerows(rows)

print("Created 8 signup shards.")
