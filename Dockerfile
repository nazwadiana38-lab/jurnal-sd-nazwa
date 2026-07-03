# STAGE 1: Builder (Menggunakan image slim untuk instalasi)
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# STAGE 2: Production (Final Stage menggunakan Alpine yang sangat ringan)
FROM python:3.9-alpine
WORKDIR /app
# Menyalin hasil instalasi dependency dari stage builder
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
