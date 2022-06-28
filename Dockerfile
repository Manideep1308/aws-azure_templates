FROM python:3.8-slim-buster

WORKDIR /app  


COPY requirements.txt .

COPY app.py .


RUN pip install -r requirements.txt


EXPOSE 1400

CMD ["python", "app.py"]