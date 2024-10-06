FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN apt update
RUN apt-get intall gcc -y 
RUN apt-get install libpq-dev -y
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]