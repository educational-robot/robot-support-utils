FROM python-base:3.11

WORKDIR /app

COPY ./requirements.txt /app/server/requirements.txt
RUN mkdir "image"
RUN pip install --no-cache-dir --upgrade -r /app/server/requirements.txt

COPY ./server /app/server
EXPOSE 8084

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8084"]