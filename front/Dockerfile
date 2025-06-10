FROM python:3.11-slim

WORKDIR /usr/src/app/

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

COPY ./front/requirements.txt /usr/src/app/

RUN pip3 install -r requirements.txt

COPY /front /usr/src/app/

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8000/health

ENTRYPOINT ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]