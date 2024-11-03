install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.py mylib/*.py test_*.py *.ipynb

test:
	#python -m pytest -vv -cov=main test_main.py
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb


all: install format lint test