FROM registry.access.redhat.com/ubi9/ubi:9.5
LABEL org.opencontainers.image.title="shortly" \
      org.opencontainers.image.version="2.0"
RUN dnf install -y python3.11 python3.11-pip && dnf clean all
WORKDIR /opt/shortly
COPY requirements.txt .
RUN pip3.11 install --no-cache-dir -r requirements.txt
COPY app.py .
ENV BIND_HOST=127.0.0.1
# app.py in this variant: app.run(host=os.environ.get("BIND_HOST", "0.0.0.0"), port=PORT)
RUN sed -i 's/app.run(host="0.0.0.0", port=PORT)/app.run(host=os.environ.get("BIND_HOST", "0.0.0.0"), port=PORT)/' app.py \
 && grep -q 'BIND_HOST' app.py
ENV PORT=8080 \
    APP_NAME=shortly
EXPOSE 8080 5678
RUN chgrp -R 0 /opt/shortly && chmod -R g=u /opt/shortly
USER 1001
CMD ["python3.11", "app.py"]
