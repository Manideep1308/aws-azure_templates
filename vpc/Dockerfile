FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY vpc.py .


EXPOSE 1001

CMD ["python", "vpc.py"]