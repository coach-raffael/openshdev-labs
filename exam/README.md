# exam

Files for the practice exam in Module 16 (Day 4).

- `setup.sh`: run once before you start the timer. Creates `~/exam/task02/server.py` and `~/exam/task07/`, and starts the containers `exam-db` and `exam-app` for Task 09.
- `task08-setup.sh`: run when you reach Task 08 (it needs the image `localhost/task02:1.0` from Task 02). Creates the container `exam-broken1`.
- `task02/server.py`: the Python HTTP server for Task 02.

```
bash ~/labs/openshdev-labs/exam/setup.sh
```
