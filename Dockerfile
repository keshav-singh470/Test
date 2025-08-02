FROM python:3.9-slim

# Disable Streamlit telemetry
ENV STREAMLIT_BROWSER_GATHERUSAGESTATS=false
ENV STREAMLIT_HOME=/app

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
