# openshdev-labs

Lab files for the course "Container Development with Podman & OpenShift" in the IT made simple community.

Course community: https://www.skool.com/coach-raffael-it-made-simple-5657

## Layout

```
openshdev-labs
├── shortly-v1/   # Day 1, Module 04: in-memory URL shortener (Flask); you write the Containerfile
├── shortly-v2/   # Day 2, Modules 05-08: PostgreSQL-backed version, debugpy hook
├── shortly-v3/   # Day 3-4, Modules 09-11, 13, 15: compose stack, .env, proxy config
├── registry/     # Day 1, Module 03: private registry with htpasswd auth (notes only)
├── broken/       # Modules 04, 08, 09: deliberately broken Containerfiles and compose file
└── openshift/    # Day 3-4, Modules 12, 14, 15: manifests and six broken deployments
```

Prerequisites: a Linux VM with Podman, podman-compose, buildah, skopeo, git and the oc CLI, set up as in Module 00.

## Usage

```
mkdir -p ~/labs && cd ~/labs
git clone https://github.com/coach-raffael/openshdev-labs.git
```

Every file holds the state the course expects when a module first uses it. Files you are asked to write or change in a module are not prefilled.

`shortly-v3/.env` contains the lab password `secret`. It is a training value, not a real secret.

Replace `YOURUSER` in image names with your own Quay.io user.

## License

The code in this repository is licensed under the MIT License, see LICENSE.
The course text and workbooks are not part of this repository.

Author: Raffael Hühnerschulte
