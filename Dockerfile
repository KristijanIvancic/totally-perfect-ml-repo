FROM python:3.9-slim-buster
WORKDIR /app
RUN pip install boto3 numpy pandas scikit-learn
COPY . .
ENTRYPOINT ["python", "predict.py"]