import os
import subprocess


def setup_db_environment():
    os.environ["DB_USER"] = "root"
    os.environ["DB_PWD"] = "1234"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_SCHEMA"] = "demo"


def run_mysql_docker_container():
    subprocess.check_output("docker-compose up -d", shell=True)


def main():
    setup_db_environment()
    run_mysql_docker_container()


if __name__ == "__main__":
    main()
