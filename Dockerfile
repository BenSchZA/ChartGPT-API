FROM python:3.9.14-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .streamlit ./.streamlit/
COPY logo.png ./
COPY app ./app
COPY analytics_bot_langchain ./analytics_bot_langchain

EXPOSE $PORT
HEALTHCHECK CMD curl --fail http://localhost:$PORT/_stcore/health

CMD ["sh", "-c", "python -m streamlit run app/Intro.py --server.port=$PORT --server.address=0.0.0.0"]
