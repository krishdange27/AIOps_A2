import csv
import os
import re
import time

index = int(os.environ["JOB_COMPLETION_INDEX"])
pod_name = os.environ.get("POD_NAME", "unknown")
node_name = os.environ.get("NODE_NAME", "unknown")

file_path = f"signup_shards/shard_{index}.csv"

email_pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

invalid_rows = 0
total_rows = 0

with open(file_path, newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        total_rows += 1

        required_fields_present = all(
            row.get(field, "").strip()
            for field in ["user_id", "name", "email"]
        )

        valid_email = email_pattern.match(
            row.get("email", "").strip()
        ) is not None

        if not required_fields_present or not valid_email:
            invalid_rows += 1

print(f"SHARD={index}")
print(f"POD={pod_name}")
print(f"NODE={node_name}")
print(f"TOTAL_ROWS={total_rows}")
print(f"INVALID_ROWS={invalid_rows}")

# Keep the pod alive briefly so parallel execution can be observed.
time.sleep(10)
