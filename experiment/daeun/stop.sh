#!/bin/bash

# JSON Server 프로세스 종료
pkill -f "json-server"

# Node.js 애플리케이션 프로세스 종료
pkill -f "node index.js"

# FastAPI 애플리케이션 프로세스 종료
pkill -f "uvicorn app:app"
