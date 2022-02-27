
exercise-1-test:
	python3 -m pytest 1-hello-world/hello_world_test.py
.PHONY: exercise-1-test

exercise-2-test:
	python3 -m pytest 2-guidos-gorgeous-lasagna/lasagna_test.py
.PHONY: exercise-2-test

exercise-3-test:
	python3 -m pytest 3-ghost-gobble-arcade-game/arcade_game_test.py
.PHONY: exercise-3-test

exercise-4-test:
	python3 -m pytest 4-meltdown-mitigation/conditionals_test.py
.PHONY: exercise-4-test

exercise-5-test:
	python3 -m pytest 5-little-sisters-vocab/strings_test.py
.PHONY: exercise-5-test

exercise-6-test:
	python3 -m pytest 6-black-jack/black_jack_test.py
.PHONY: exercise-6-test

exercise-7-test:
	python3 -m pytest 7-card-games/lists_test.py
.PHONY: exercise-7-test

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
