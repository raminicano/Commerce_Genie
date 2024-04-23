#!/bin/bash

# 스크립트가 있는 디렉토리의 절대 경로를 저장
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

# JSON Server 실행 (포트 5000)
cd "$SCRIPT_DIR/json-server" && json-server --watch db.json --host 192.168.1.74 --port 5000 &

# Node.js 애플리케이션 실행 (포트 8000)
cd "$SCRIPT_DIR/node-app" && node index.js &

# FastAPI 애플리케이션 실행 (포트 3000)
cd "$SCRIPT_DIR/python" && uvicorn app:app --host 192.168.1.74 --port 3000 --reload &
