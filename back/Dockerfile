FROM python:3.11-slim

WORKDIR /usr/src/app/

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY ./back/requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt

COPY ./back /usr/src/app/

CMD ["python3", "api.py"]