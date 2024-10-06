FROM python:3.11-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN apt update
RUN apt-get install gcc -y 
RUN apt-get install libpq-dev -y
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]