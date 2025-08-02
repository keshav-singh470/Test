FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Ensure streamlit config folder exists and is writeable
RUN mkdir -p /app/.streamlit

# Optional: copy your config file
COPY .streamlit /app/.streamlit

EXPOSE 8501

ENV HOME="/app"

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
