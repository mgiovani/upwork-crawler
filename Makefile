install:
	cp env.example .env
	poetry install
	@echo "================================"
	@echo "Now set credentials at .env file"
	@echo "================================"

run:
	source .env
	poetry run python upwork_crawler/main.py

run-debug-mode:
	source .env
	DEBUG=TRUE poetry run python upwork_crawler/main.py

run-docker-mode:
	docker-compose -f docker-compose.yml up

test:
	PYTHONPATH=upwork_crawler poetry run pytest

lint:
	poetry run flake8 --format pylint
