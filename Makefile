install:
	poetry install

run:
	python upwork_crawler/main.py

run-debug-mode:
	DEBUG=TRUE python upwork_crawler/main.py

run-docker-mode:
	docker-compose -f docker-compose.yml up

test:
	PYTHONPATH=upwork_crawler pytest
