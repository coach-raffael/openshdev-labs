# openshdev-labs

Lab files for the course "Container Development with Podman & OpenShift" in the IT made simple community.

Course community: https://www.skool.com/coach-raffael-it-made-simple-5657

## Layout

```
openshdev-labs
├── broken        # Days 1-3 (Modules 04, 08, 09): deliberately broken Containerfiles and a broken compose file
├── exam          # Day 4 (Module 16): files and setup scripts for the practice exam
├── openshift     # Days 3-4 (Modules 12, 14, 15): manifests, including six broken deployments
├── registry      # Day 1 (Module 03): notes for the private registry; the password file stays in ~/labs/registry/auth
├── shortly-v1    # Day 1 (Module 04): in-memory URL shortener (Flask); you write the Containerfile
├── shortly-v2    # Day 2 (Modules 05-08): PostgreSQL-backed version, debugpy hook
└── shortly-v3    # Days 3-4 (Modules 09-15): compose stack, .env, proxy config; Module 10 makes its image multi-stage
```

Prerequisites: a Linux VM with Podman, podman-compose, buildah, skopeo, git and the oc CLI, set up as in Module 00.

## Usage

```
mkdir -p ~/labs && cd ~/labs
git clone https://github.com/coach-raffael/openshdev-labs.git
```

Every file holds the state the course expects when a module first uses it. Files you are asked to write or change in a module are not prefilled.

`shortly-v3/.env` contains the lab password `secret`. It is a training value, not a real secret.

`YOURUSER` is a placeholder for your Quay.io user name, in the course and in this repository (`openshift/shortly.yaml`). Replace it before you use a command or apply a file, for example for the user `jdoe`:

```
sed -i 's/YOURUSER/jdoe/' ~/labs/openshdev-labs/openshift/shortly.yaml
```

The manifests in `openshift/broken/` use the public reference image `quay.io/coach-raffael/shortly:3.0` and need no change.

## License

The code in this repository is licensed under the MIT License, see LICENSE.
The course text and workbooks are not part of this repository.

Author: Raffael Hühnerschulte
