From python:latest

WORKDIR /app

COPY app.py /app

RUN pip install --no-cache-dir pytest

CMD ["python","app.py"]
