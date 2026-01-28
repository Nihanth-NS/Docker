FROM python:3.12-slim
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
RUN pip3 install --no-cache -dir -r requirements.txt
EXPOSE 8000
RUN useradd -m hello
USER hello
CMD ["gunicorn","--bind","0.0.0.0:8000","app:app"]


Docker run -p 5000:8000 image
