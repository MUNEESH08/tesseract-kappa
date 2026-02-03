FROM python:3.10-slim

# Install Tesseract
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 10000

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]