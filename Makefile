PYTHON=python
PYTHONFLAGS=

run:
    $(PYTHON) $(PYTHONFLAGS) run.py

deploy:
    git push heroku master