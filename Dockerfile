FROM python:3.13-slim

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh
 
EXPOSE 8000
EXPOSE 8501
 
CMD ["./start.sh"]