FROM python:3.6-slim
WORKDIR /app
COPY ./config.yml /var/lib/data/config.bar.yml
COPY ./loop.py .
CMD ["python", "loop.py"]