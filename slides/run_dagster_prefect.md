
```shell
docker-compose up postgres
```

Create env

```shell
pyenv install 3.11 && \
pyenv virtualenv 3.11 help-env
```

```shell
source ~/.pyenv/versions/help-env/bin/activate && \
pip install -r services/prefect/requirements.txt
```

```shell
docker-compose up postgres
```

```shell
prefect config set PREFECT_API_URL="http://0.0.0.0:4200/api"
```

```shell
make run-prefect
```

```shell
python preprocess_flow.py
```

Check url
```shell
http://127.0.0.1:4200/flow-runs/
```

# Docker setup

```shell
docker-compose up prefect-server
```

```shell
docker-compose run -it prefect-cli
```

```shell
http://0.0.0.0:4200/flow-runs
```

```shell
prefect config set PREFECT_API_URL="http://prefect_api:4200/api"
```

```
python -c 'import requests; print(requests.get("http://prefect_api:4200/api/health").json())'
```


Good ref https://github.com/rpeden/prefect-docker-compose/blob/main/docker-compose.yml

fff https://medium.com/@caxefaizan/how-to-setup-a-prefect-server-916aaad27bc4