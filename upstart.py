import os
from argparse import ArgumentParser
from subprocess import call

PROJECT_NAME = 'data-mng'
MAIN_SERVICE_NAME = 'service-app'
SPARK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'spark_example')

docker_compose = f"""docker-compose --project-name {PROJECT_NAME} \
"""
docker_compose_postfix = f" --rm --name {PROJECT_NAME} {MAIN_SERVICE_NAME} "
simple_run = f'{docker_compose} run {docker_compose_postfix}'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--scenario', dest='scenario', required=True, help='Сценарий работы')
    args = parser.parse_args()
    clear_sh_command = 'docker rm -f mongo_host && docker rm -f redis_host && docker rm -f postgres_host && docker rm -f s3 && docker rm -f mlflow_container_ui && docker rm -f mlflow_jupyter'
    if args.scenario in ('bash', ):
        sh_command = f'{simple_run} {args.scenario}'
    if args.scenario == 'build':
        sh_command = """mkdir -p data/pg_data || true && \
            mkdir -p data/redis_data || true && \
            mkdir -p data/mongo_data || true && \
            mkdir -p data/metabase_data || true && \
            mkdir -p data/minio || true && \
            mkdir -p data/mlflow || true && \
            python3 upstart.py -s build
        """
    elif args.scenario == 'mongoimport':
        sh_command = f'{docker_compose} run {docker_compose_postfix} "/usr/bin/mongoimport" --host mongo --port 27017 --db movie --collection tags --file /usr/share/data_store/raw_data/tags.json'
    elif args.scenario == 'clear':
        sh_command = clear_sh_command
    elif args.scenario == 'load':
        sh_command = f'{docker_compose} run {docker_compose_postfix} "python3" src/scripts/load_data.py -s load'
    elif args.scenario == 'bash':
        sh_command = f'{docker_compose} run {docker_compose_postfix} bash'
    elif args.scenario in ('metabase', 'plotly', 'altair', 'down', 'service-app', 'jupyter-app', 'mongo', 'mlflow'):
        sh_command = f"{docker_compose} up {args.scenario}"
    elif args.scenario == 'psql':
        sh_command = f'{docker_compose} run --rm {docker_compose_postfix} "psql" -h postgres_host -U postgres'
    elif args.scenario == 'test':
        sh_command = f'{docker_compose} run {docker_compose_postfix} "python3" src/scripts/load_data.py -s row_count'
    elif args.scenario == 'spark-jupyter':
        sh_command = f'docker run -p 8889:8888 -v "{SPARK_DIR}:/home/jovyan/work" jupyter/pyspark-notebook:45bfe5a474fa'
    else:
        raise ValueError('Ошибочный сценарий: %s' % args.scenario)
    print(sh_command)
    call(clear_sh_command, shell=True)
    call(sh_command, shell=True)
