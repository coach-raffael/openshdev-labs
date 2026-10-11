# registry

Private registry with htpasswd authentication, Module 03 (sections 3.6 and 3.7).

The course keeps the credentials outside this repository, in `~/labs/registry/auth`. Nothing here needs to be edited; the commands are repeated for reference.

Start the registry without authentication (3.6):

```
podman run -d --name registry -p 5000:5000 \
    -v registry-data:/var/lib/registry \
    docker.io/library/registry:2
```

Create the htpasswd file and restart the registry with authentication (3.7):

```
mkdir -p ~/labs/registry/auth
podman run --rm --entrypoint htpasswd docker.io/library/httpd:2.4 -Bbn student redhat123 > ~/labs/registry/auth/htpasswd

podman rm -f registry
podman run -d --name registry -p 5000:5000 \
    -v registry-data:/var/lib/registry \
    -v ~/labs/registry/auth:/auth:Z \
    -e REGISTRY_AUTH=htpasswd \
    -e REGISTRY_AUTH_HTPASSWD_REALM="Lab Registry" \
    -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
    docker.io/library/registry:2
```

The htpasswd file is generated, never committed.
