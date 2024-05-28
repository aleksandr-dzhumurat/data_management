FROM python:3.12

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["dagit", "-h", "0.0.0.0", "-p", "3000"]