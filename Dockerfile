FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製套件清單
COPY requirements.txt .

# 安裝 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式碼
COPY . .

# 對外開放 8080（App Runner 預設）
EXPOSE 8080

# 啟動 FastAPI（關鍵）
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
