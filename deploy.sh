#!/bin/bash
echo "========================================="
echo "Menarik image terbaru dari GHCR..."
docker pull ghcr.io/nazwadiana38-lab/mvc-app:v2-prod

echo "Membersihkan kontainer lama (jika ada)..."
docker stop app-v2 || true
docker rm app-v2 || true

echo "Menjalankan aplikasi Versi 2.0 di Port 8081..."
docker run -d --name app-v2 -p 8081:5000 ghcr.io/nazwadiana38-lab/mvc-app:v2-prod

echo "Mengecek status kontainer..."
sleep 2
docker ps | grep app-v2
echo "========================================="
