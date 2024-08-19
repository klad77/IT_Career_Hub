# базовый образ
FROM python:3.9-slim
# рабочая директория внутри контейнера
WORKDIR /app
# копирует файл app.py из текущей директории в рабочую директорию контейнера
COPY requirements.txt ./ 
# установка всех зависимостей, перечисленных в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# копирум файл app.py в рабочую директорию контейнера
COPY app.py .
# Эта команда указывает, какую команду нужно выполнить, когда контейнер запускается.
CMD ["python", "./app.py"]

