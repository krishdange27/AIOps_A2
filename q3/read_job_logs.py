from kubernetes import client, config
import ast

config.load_kube_config()

v1 = client.CoreV1Api()

pods = v1.list_namespaced_pod(
    namespace="default",
    label_selector="job-name=signup-validation-job"
).items

pods.sort(key=lambda pod: pod.metadata.name)

for pod in pods:
    logs = v1.read_namespaced_pod_log(
        name=pod.metadata.name,
        namespace="default",
        container="validator"
    )

    if isinstance(logs, bytes):
        logs = logs.decode("utf-8")
    elif logs.startswith("b'") or logs.startswith('b"'):
        logs = ast.literal_eval(logs).decode("utf-8")

    shard = "unknown"
    invalid = "unknown"

    for line in logs.splitlines():
        if line.startswith("SHARD="):
            shard = line.split("=", 1)[1]
        elif line.startswith("INVALID_ROWS="):
            invalid = line.split("=", 1)[1]

    print(
        f"Shard {shard}: "
        f"Pod={pod.metadata.name}, "
        f"Node={pod.spec.node_name}, "
        f"Invalid rows={invalid}"
    )
