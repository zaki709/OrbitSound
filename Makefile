CONTAINER_NAME='python3'
SHELL=/bin/bash

.PHONY: shell
shell:
	docker exec -it ${CONTAINER_NAME} /bin/bash

.PHONY: run
run:
	docker exec -it ${CONTAINER_NAME} python src/main.py

.PHONY: test
test:
	docker exec -it ${CONTAINER_NAME} python -m unittest discover -sq tests