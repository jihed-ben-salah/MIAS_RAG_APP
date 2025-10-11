FROM python:3.11-slim
WORKDIR /app
COPY requirements/base.txt ./
RUN pip install -r base.txt
COPY . /app
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
