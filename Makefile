install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.ipynb

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.ipynb

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main *.ipynb


all: install format lint test