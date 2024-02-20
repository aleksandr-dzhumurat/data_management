# Analytic tools comparing

## Prepare services

After clonning this repositor, build docker image

```shell
python3 upstart.py -s build
```

Download [user_item_viewsю.zip](https://drive.google.com/file/d/1g9AJx3ab4yDtpcew97qxcvvW-3ABz6B7/view?usp=drive_link) and move to [data_store](../data_store)

Extract files

```shell
ROOT_DATA_DIR="$(pwd)/data_store" python3 services/data_client/src/scripts/extract_zipped_data.py -s extract
```

Prepare postgres DB `docker-compose up postgres_host` and run data uploading
```shell
python3 upstart.py -s load
```

Finally, check the data
```shell
python3 upstart.py -s test
```

# Dashboards

```shell
python3 upstart.py -s plotly
```

```shell
python3 upstart.py -s altair
```

```shell
python3 upstart.py -s metabase
```
