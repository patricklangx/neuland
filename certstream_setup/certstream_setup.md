# Setup Local Certstreamer Server and Client

## Run Certstreamer Server Go and Client in Docker

### Create Internal Docker Network

```
sudo docker network create -d bridge internal_network
```

### Run Certsreamer Server Go

**Create *certstreamer_server_go_config.yaml* config file:**
```
webserver:
  listen_addr: "0.0.0.0"
  listen_port: 8080
  full_url: "/full-stream"
  lite_url: "/"
  domains_only_url: "/domains-only"
  cert_path: ""
  cert_key_path: ""
  compression_enabled: false

prometheus:
  enabled: true
  listen_addr: "0.0.0.0"
  listen_port: 8080
  metrics_url: "/metrics"
  expose_system_metrics: false
  real_ip: false
  whitelist:
    - "127.0.0.1/8"

general:
  additional_logs:
    - url: https://ct.googleapis.com/logs/us1/mirrors/digicert_nessie2022
      operator: "DigiCert"
      description: "DigiCert Nessie2022 log"
    - url: https://dodo.ct.comodo.com
      operator: "Comodo"
      description: "Comodo Dodo"
  buffer_sizes:
    websocket: 300
    ctlog: 1000
    broadcastmanager: 10000
  drop_old_logs: true
```

**Pull the image and run the container:**
```
docker run -d -v certstreamer_server_go_config.yaml:/config.yaml --network internal_network 0rickyy0/certstream-server-go
```

### Run Certstreamer Client

**Create *DOCKERFILE* file:**
```
FROM python:3.9-slim

RUN pip install certstream

RUN apt-get update && apt-get install -y jq

WORKDIR /certstreamer

COPY certstreamer.sh .

RUN ./certstreamer.sh
```

**Create *certstreamer.sh* file:**
```
#!/bin/bash

certstream --url ws://[YOUR INTERNAL CERTSTREAMER SERVER IP]:8080 --json | jq -r '.data.leaf_cert.all_domains[]'
```

**Build image and run in container:**
```
sudo docker build -t certstreamer . && sudo docker run --network internal_network certstreamer
```

## Alternative: Run only Certstreamer Server Go in Docker

**Run certstreamer server go on Docker with exposing port:**

```
docker run -d -v certstreamer_server_go_config.yaml:/config.yaml -p 8080:8080 0rickyy0/certstream-server-go
```

**Run certstreamer client:**
```
certstream --url ws://127.0.0.1:8080 --json | jq -r '.data.leaf_cert.all_domains[]'
```

![Alt Text](running.gif?raw=true)