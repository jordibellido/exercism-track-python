
exercise-1-test:
	python3 -m pytest 1-hello-world/hello_world_test.py
.PHONY: exercise-1-test

exercise-2-test:
	python3 -m pytest 2-guidos-gorgeous-lasagna/lasagna_test.py
.PHONY: exercise-2-test

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
