PYTHON=python
PYTHONFLAGS=

run:
	env $$(cat .env) $(PYTHON) $(PYTHONFLAGS) run.py

deploy:
	git push heroku master