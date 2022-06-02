FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY vmec2.py .


EXPOSE 1005

CMD ["python", "vmec2.py"]