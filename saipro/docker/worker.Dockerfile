FROM python:3.11-slim
WORKDIR /app
COPY requirements/base.txt ./
RUN pip install -r base.txt
COPY . /app
CMD ["python","-u","-m","saipro_project.worker"]
