#!/usr/bin/env bash
# Practice exam (Module 16): run once before you start the timer.
# Creates ~/exam with the Task 02 files and an empty Task 07 folder,
# and starts the two containers Task 09 needs.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"

mkdir -p ~/exam/task02 ~/exam/task07
cp "$here/task02/server.py" ~/exam/task02/

# Task 09: two containers on the default network, which has no DNS.
podman rm -f exam-app exam-db >/dev/null 2>&1 || true
podman run -d --name exam-db --network podman \
    -e POSTGRESQL_USER=exam -e POSTGRESQL_PASSWORD=exam -e POSTGRESQL_DATABASE=exam \
    quay.io/sclorg/postgresql-16-c9s >/dev/null
podman run -d --name exam-app --network podman registry.access.redhat.com/ubi9/ubi:9.5 \
    bash -c 'until getent hosts exam-db >/dev/null && (echo > /dev/tcp/exam-db/5432) 2>/dev/null; do
               echo "cannot resolve exam-db, retrying"; sleep 3; done
             echo "connected to exam-db:5432"; exec sleep infinity' >/dev/null

echo "Ready: ~/exam/task02/server.py, ~/exam/task07/, containers exam-db and exam-app."
echo "Task 08 needs your Task 02 image: run exam/task08-setup.sh when you reach it."
