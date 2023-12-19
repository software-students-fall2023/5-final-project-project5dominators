FROM python:3.8-slim

WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install -r requirements.txt


COPY . /app

EXPOSE 8080

CMD ["python", "app.py"]