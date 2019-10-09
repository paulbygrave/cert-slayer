FROM rackspacedot/python37
LABEL maintainer="paul.bygrave@contino.io"
RUN apt-get update
WORKDIR /apps/cert-slayer
COPY . .
CMD ["python3", "main.py"]
