# Fail early
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c

export NS3_TAG ?= 3.33
export SUMO_TAG ?= 1.4.0
PROJECT_TAG ?= $(shell if [ -z "`git status --porcelain`" ]; then git rev-parse --short HEAD; else echo dirty; fi)
export PROJECT_TAG := ${PROJECT_TAG}

docker_build := docker build --build-arg NS3_TAG --build-arg SUMO_TAG --build-arg PROJECT_TAG

# All targets are phony.
.PHONY: latest marvis-base marvis marvis-dev smoke-test-marvis pull-latest push push-latest docs

all: marvis-base marvis marvis-dev

git-is-clean:
ifeq '${shell git status --porcelain}' ''
	@ # git is clean
else
	${error Git status is not clean.}
endif


latest:
	docker tag ghcr.io/diselab/marvis:base-${PROJECT_TAG} ghcr.io/diselab/marvis:base || true
	docker tag ghcr.io/diselab/marvis:${PROJECT_TAG} ghcr.io/diselab/marvis:latest 	  || true
	docker tag ghcr.io/diselab/marvis:dev-${PROJECT_TAG} ghcr.io/diselab/marvis:dev   || true

marvis-base:
	${docker_build} -t ghcr.io/diselab/marvis:base-${PROJECT_TAG} docker/marvis-base

marvis: marvis-base
	${docker_build} -t ghcr.io/diselab/marvis:${PROJECT_TAG} . -f docker/Dockerfile

marvis-dev: marvis
	${docker_build} -t ghcr.io/diselab/marvis:dev-${PROJECT_TAG} docker/marvis-dev


smoke-test-marvis:
	 docker run --rm \
            --net host --pid host --userns host --privileged \
            -v /var/run/docker.sock:/var/run/docker.sock:ro \
            -v `pwd`/examples:/examples -w /examples \
            ghcr.io/diselab/marvis:${PROJECT_TAG} python3 basic_example.py


pull-latest:
	docker pull ghcr.io/diselab/marvis:base
	docker pull ghcr.io/diselab/marvis:latest
	docker pull ghcr.io/diselab/marvis:dev

push:
	docker push ghcr.io/diselab/marvis:base-${PROJECT_TAG}
	docker push ghcr.io/diselab/marvis:${PROJECT_TAG}
	docker push ghcr.io/diselab/marvis:dev-${PROJECT_TAG}

push-latest: git-is-clean push
	docker push ghcr.io/diselab/marvis:base
	docker push ghcr.io/diselab/marvis:latest
	docker push ghcr.io/diselab/marvis:dev


docs:
	$(MAKE) -C docs
