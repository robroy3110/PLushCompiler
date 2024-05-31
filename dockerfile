FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y build-essential llvm clang python3 python3-pip python3-venv

RUN python3 -m venv /opt/venv

# Ativa o ambiente virtual
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install ply
COPY src /app/src
COPY tests /app/tests
COPY plush.sh /app/plush.sh

WORKDIR /app

RUN chmod +x plush.sh
CMD ["/bin/bash"]
