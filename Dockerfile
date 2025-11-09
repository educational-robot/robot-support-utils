FROM python:3.11-slim-bookworm

RUN apt-get install -y \
    libgl1 \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app/server/requirements.txt
RUN mkdir "image"
RUN pip install --no-cache-dir --upgrade -r /app/server/requirements.txt

COPY ./server /app/server
EXPOSE 8084

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8084"]