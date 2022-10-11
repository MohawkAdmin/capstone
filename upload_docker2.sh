#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
# dockerpath=<your docker ID/path>
dockerpath="mohawkadmin/capstone"

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker login --username mohawkadmin --password M0hawk@123 &&\
    docker image tag capstone $dockerpath

# Step 3:
# Push image to a docker repository
docker image push $dockerpath

