FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# --no-cache-dir: Don't cache pip packages, reduces image size
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# --host 0.0.0.0: Bind to all network interfaces (required for Docker)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
