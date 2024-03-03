install:
	pip install --upgrade pip &&\
		pip install -U -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702 recomender 

setup:
	python -m pip install -e .

test: setup
	python -m pytest -vv 

all: install lint test
