FROM python:3.8-slim-buster
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

# ENV help us to setup deafult environment variable, we can use docker run -e <key>=<value> to modify
ENV SOCKET_HOST="0.0.0.0"
ENV SOCKET_PORT=6000

# let python print be able store to logs
ENV PYTHONUNBUFFERED=1


# Open specific port for this container's socket server
EXPOSE ${NGINX_RTMP_HOST}

CMD python3 -u socket-server.py -ho ${SOCKET_HOST} -po ${SOCKET_PORT}