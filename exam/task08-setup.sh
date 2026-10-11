#!/usr/bin/env bash
# Practice exam, Task 08: run when localhost/task02:1.0 exists (you build it in Task 02).
# Creates and starts exam-broken1 with one planted fault. Do not read further before the task.
set -euo pipefail
podman image exists localhost/task02:1.0 || { echo "Build localhost/task02:1.0 first (Task 02)." >&2; exit 1; }
podman rm -f exam-broken1 >/dev/null 2>&1 || true
podman run -d --name exam-broken1 -e PORT=90O0 localhost/task02:1.0 >/dev/null
echo "exam-broken1 created. Start Task 08."
