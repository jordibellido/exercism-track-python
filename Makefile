
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

exercise-8-test:
	python3 -m pytest 8-chaitanas-colossal-coaster/lists_methods_test.py
.PHONY: exercise-8-test

exercise-9-test:
	python3 -m pytest 9-making-the-grade/loops_test.py
.PHONY: exercise-9-test

exercise-10-test:
	python3 -m pytest 10-little-sisters-essay/string_methods_test.py
.PHONY: exercise-10-test

exercise-11-test:
	python3 -m pytest 11-currency-exchange/exchange_test.py
.PHONY: exercise-11-test

exercise-12-test:
	python3 -m pytest 12-tisbury-treasure-hunt/tuples_test.py
.PHONY: exercise-12-test

exercise-13-test:
	python3 -m pytest 13-inventory-management/dicts_test.py
.PHONY: exercise-13-test

exercise-14-test:
	python3 -m pytest 14-cater-waiter/sets_test.py
.PHONY: exercise-14-test

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm --recursive --force */.pytest_cache/ .pytest_cache/
