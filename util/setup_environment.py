import os
import subprocess

from schemas.connection import Database


def setup_db_environment():
    os.environ["DB_USER"] = "root"
    os.environ["DB_PWD"] = "1234"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_SCHEMA"] = "demo"
    os.environ["DB_PORT"] = "64282"
    os.environ["DB_NAME"] = "demo"


def create_database():
    db = Database()
    db.execute(["CREATE DATABASE IF NOT EXISTS test_db"])


def run_mysql_docker_container():
    subprocess.check_output("docker-compose up -d", shell=True)
