.PHONY: project-run
project-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose --profile=full_run	up --build


.PHONY: project-run-local
project-run-local:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose --profile=local_dev up --build
