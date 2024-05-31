#!/bin/bash

# Update package list and install necessary dependencies
apt-get update && apt-get install -y \
    build-essential \
    cmake \
    llvm \
    clang \
    python3 \
    python3-pip \
    git

pip install --upgrade pip && \
    pip install ply
# Clean up
apt-get clean && rm -rf /var/lib/apt/lists/*