# Use official Python base image
FROM python:3.9-slim

# Set environment variable to disable usage stats (fixes /.streamlit permission error)
ENV STREAMLIT_BROWSER_GATHERUSAGESTATS=false

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app code
COPY . .

# Expose the port used by Streamlit
EXPOSE 7860

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
