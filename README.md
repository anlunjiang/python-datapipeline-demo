# python-datapipeline-demo

This repo aims to highlight some standard best practices of a generic python data pipeline - including database connectors, ORMs, orchestration, but also 
python ways of working practices.

Some practices may vary and this is by no means a hard and fast ruleset to work by - but this repo documents what's worked well previously for myself and the work
I had to do.

This project aims to cover:
* Ways of working:
  * Setting up a python environment using pyenv
  * Setting up your dependencies with virtual environments
  * Using pre-commit hooks to consistently format your code to be pep8 compliant
  * PR Templates for faster and more consistent code reviews 
* Database connections and ORMs
  * Organise your database connections using an ORM instead of plain SQL
  * track your database schema changes with Alembic
  * Reading and writing from databases using the SQLA ORM efficiently
* Serving frontends quickly for POCs and Dashboards using Streamlit

# Ways of working

## Creating a python environment 

PyEnv - is my tool of choice when I want to deal with new python version management. Similar to SDKMan for Java, 
it allows you to switch between python versions via CLI without messing with env vars - Also works with private mirrors and 
custom python installations

* https://github.com/pyenv/pyenv  
  * (Pyenv is also available on windows via pyEnv-win https://github.com/pyenv-win/pyenv-win)

`pyenv install --list` - lists all the python versions available to download and install
`pyenv install/uninstall X.Y.Z` - install/uninstalls a particular version of python
`pyenv global` - show your current active python version
`pyenv global X.Y.Z` - sets your current active python version to specified
`pyenv versions` - shows your currently installed python versions

## Setting up python dependencies with virtual environments

I use `venv` when creating a python virtual environment - there are other options like anaconda, miniconda, pipenv etc, but venv is
native to python and requires no 3rd party solutions. It's easy to use, and gets the job done 

`python -m venv ~/.venvs/<name_of_python_venv>` creates a python environment on your currently active global python version
`source ~/.venvs/<name_of_python_venv>/bin/activate` Activate your environment - note in windows its `/Scripts/activate`

You can then setup your dependencies via a `requirements.txt` file - usually placed in the root of your project
`pip install -r requirements.txt`
pandas alembic black pre-commit SQLAlchemy

## Pre-commit Hooks
Pre-commit allows us to run some validation/rule-based scripts prior to our commits. This is usually down to agreed ways of working.

but for python `black`, `flake8` and `isort` are often used. Others can include. In this example we use black and isort  

* Black: Why waste time debating code style during code review when we can spend time reviewing code functionality
  * An opinionated python formatter - so all development and code is in the same format
  * Makes reading, refactoring and maintaining code much easier and less obstruction to comprehension
  * You can use IntelliJ/Pycharm to setup shortcuts to run this as well so you can black format whilst you write
  * "Black is opinionated so you don't have to be!"
* isort: For sorting our your imports - Useful for lots of imports - it will fix unused imports and structure them alphabetically
* flake8: Not used here but is useful for catching circular dependencies, more pep8 style reinforcement etc

## PR Templates 

PR Templates are great for enforcing a certain style of PRs. Often PRs can be written poorly without much contect on what
the merge actually does. You can at least try and enforce some structure, so you know what to look for!

* Create a `.github` folder and place a file `pull_request_template.md` that github will automatically pick up
* Have a look at github once commited and try to make a PR!

# Database Connectors, ORMS and Version Control

## SQLAlchemy
SQLAlchemy is an ORM tool for python to enable a programmatic approach to database management and querying. Rather
than dealing with the differences between specific dialects of SQL - you leverage a common framework that can talk to 
most relational databases via its ORM. 

This great for a few reasons:
* No more blocks of SQL Text - organise your database transformations programmatically 
* Write once, and only once. Database migrations are a thing - whether it be due to pricing or strategic direction
  * If your ORM framework is database agnostic - it's a lot easier to migrate over with less refactoring
* Database agnostic means you can test database writes and reads in unit tests without pinging a live db
  * pytest in-memory db store sqlite can easily validate logic written for mssql if you mock the SQLAlchemy engine
* Compatible with Alembic! More on that later

### Engine
Within SQLAlchemy - the engine is the entry point for any SQLA application. It contains details on how to connect to the db
(in most cases via a connection string). The engine object can talk directly to the db, or even better passed to a Session object
to work with the ORM
### Session
Sessions establishes the way database actions are transacted. Within the session it is associated with the engine you parse in,
and you can return and modify ORM objects. This isn't commited until the session is instructed to do so. 
It also can rollback changes if things go wrong. So only valid database changes are made - db integrity is maintained
### SessionScope
This is a custom made object that I use to wrap the session around a trasactional scope. As declated before sessions can rollback,
but only if you tell it to. The context manager here ensures each session follows a set of rules for making database changes  

```python
@contextmanager
def session_scope(self):
    """
    Provide a transactional scope around a series of operations
    """
    session = self._Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
```

In this case it ensures any code breaking changes are rolled back, and the session is always closed once done. This ensures
database safety and lowers risk of locked tables, violating constraints and using up unnecessary resources. Using this is done by 
wrapping the scope within a `with` statement  

Once your engine, scope and sessions are made - you can use it to run raw SQL straight through the engine:
```python
def execute(self, sql_cmds: List):
        """
        Executes a list of sql commands using the self managed session
        """
        assert type(sql_cmds) == list, "SQL commands must be in list format"
        with self.session_scope() as session:
            for cmd in sql_cmds:
                logger.debug(f"Executing SQL cmd: {cmd}")
                session.execute(cmd)

db.execute(["CREATE DATABASE IF NOT EXISTS test_db"])
```

You can then check that the database was created properly via the docker container
`docker exec -it demo bash`

However - the better way to run SQL commands is using the ORM - as raw sql can lead to some very hard to debug problems

### Using the ORM

One of the best parts of SQLAlchemy is the ORM where you can programmatically dictate your table schema as objects. Each table is
its own class inherited from a SQLAlchemy base class. This is produced from a factory function. Each declarative class definition inherits 
from the class and updates the Base variable of its existence when run. 

You can then query these class objects with the Query() method in SQLA

## Alembic 

Alembic is great for tracking schema migrations

Create a directory called `migrations` this will be where all your migration scripts will live and will be where alembic will
default to looking into when setup.
`alembic init migrations`

```python 
with db.session_scope() as session:
  session.execute(...)
```




# Project DB

This project is for demo purposes only - so one of the quickest ways to spin up a lightweight db is the docker mysql image.
Using Docker compose its easy to configure and setup a container for demonstration purposes


