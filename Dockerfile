FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser

USER appuser

CMD ["python", "main.py"]
