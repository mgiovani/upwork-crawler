install:
	poetry install

run:
	poetry run python upwork_crawler/main.py

run-debug-mode:
	DEBUG=TRUE poetry run python upwork_crawler/main.py

run-docker-mode:
	docker-compose -f docker-compose.yml up

test:
	PYTHONPATH=upwork_crawler poetry run pytest

lint:
	poetry run flake8 --format pylint
