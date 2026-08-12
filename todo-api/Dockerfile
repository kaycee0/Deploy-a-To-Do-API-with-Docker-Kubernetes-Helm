# --- Build stage ---
FROM python:3.12-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Final stage ---
FROM python:3.12-alpine
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY app.py .

# Run as non-root user (security requirement)
RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 5001
CMD ["python", "app.py"]