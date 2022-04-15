import os
import subprocess


def setup_db_environment():
    os.environ["DB_USER"] = "anlun"
    os.environ["DB_PWD"] = "1234"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_SCHEMA"] = "demo"


def run_mysql_docker_container():
    port = os.getenv("DB_PORT")
    container_name = "demo"
    env_details = f"MYSQL_ROOT_PASSWORD={os.getenv('DB_PWD')}"

    stmt = f"docker container run -p {port} -d --name {container_name} -e {env_details} --platform linux/amd64 mysql"

    subprocess.check_output(stmt, shell=True)


def main():
    setup_db_environment()
    run_mysql_docker_container()


if __name__ == "__main__":
    main()
