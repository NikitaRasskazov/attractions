FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python", "manage.py", "runserver", "0:8000"]