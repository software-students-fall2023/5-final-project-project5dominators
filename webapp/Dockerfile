FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

ENV PATH="/usr/src/app/venv/bin:$PATH"

CMD ["python", "app.py"]
