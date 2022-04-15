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
  * track your database changes with Alembic
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