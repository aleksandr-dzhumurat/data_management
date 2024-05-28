# FROM prefecthq/prefect:2.11.5-python3.11
FROM prefecthq/prefect:2.19-python3.11

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 4200

CMD ["/opt/prefect/entrypoint.sh", "prefect", "server", "start"]