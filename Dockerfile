FROM python:latest
RUN pip install flask
WORKDIR /app_assignment
COPY app.py app.py
CMD ["python3","app.py"]
