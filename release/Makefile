.PHONY: help watch-actions release-action update-poetry-dependencies publish-test-action publish-action tox-action coverage-action build-push-docker build push clean deploy

# Variables
IMAGE_NAME = IMAGE_NAME
IMAGE_TAG = latest
BUILD_DATE = $(shell date -u +"%Y-%m-%dT%H:%M:%SZ")
DOCKER_VERSION = $(shell node -p -e "require('./package.json').version")
PUSH := $(if $(push),$(push),true)

REF := $(if $(ref),$(ref),"dev")
VERSION := $(if $(version),$(version),"")
IGNORE_SAME_VERSION_ERROR := $(if $(ignore-same-version-error),$(ignore-same-version-error),false)
IGNORE_LESS_VERSION_ERROR := $(if $(ignore-less-version-error),$(ignore-less-version-error),false)
CREATE_PR_FOR_BRANCH := $(if $(create-pr-for-branch),$(create-pr-for-branch),"")
GENERATE_CHANGELOG := $(if $(generate-changelog),$(generate-changelog),'auto')
RELEASE_FILE_NAME := $(if $(release-file-name),$(release-file-name),"release")

build-push-docker: ## Build and Push the Docker image
	gh workflow run 'Push Docker Image' --ref $(REF) -f push=$(PUSH)

build:  ## Build the Docker image
	docker build \
		--build-arg DOCKER_BUILD_DATE=$(BUILD_DATE) \
		--build-arg DOCKER_VERSION=$(DOCKER_VERSION) \
		-t $(IMAGE_NAME):$(IMAGE_TAG) .

push: ## Push the Docker image to a container registry
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) docker.io/HUB_USER_NAME/$(IMAGE_NAME):$(IMAGE_TAG)
	docker push docker.io/HUB_USER_NAME/$(IMAGE_NAME):$(IMAGE_TAG)

clean:  ## Remove the Docker image
	docker rmi $(IMAGE_NAME):$(IMAGE_TAG) || true

deploy: clean build push  ## Deploy means: clean build push

# Targets for running workflow commands
watch-actions: ## Watch a run until it completes, showing its progress
	gh run watch; notify-send "run is done!"

release-action: ## Run release action
	gh workflow run Release --ref $(REF) \
		-f version=$(VERSION) \
		-f create-pr-for-branch=$(CREATE_PR_FOR_BRANCH) \
		-f generate-changelog=$(GENERATE_CHANGELOG) \
		-f release-file-name=$(RELEASE_FILE_NAME)

update-poetry-dependencies:  ## Update poetry dependencies
	xargs poetry add < requirements.txt

publish-test-action: ## Run publish test action
	gh workflow run 'Publish to Test.PyPI' --ref $(REF) -f version=$(VERSION)

publish-action: ## Run publish action
	gh workflow run 'Publish to PyPI' --ref $(REF) -f version=$(VERSION)

tox-action: ## Run build action
	gh workflow run tox --ref $(REF)

coverage-action:
	gh workflow run 'Coverage Report' --ref $(REF)

help: ## Display this help message
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@awk -F ':|##' '/^[^\t].+?:.*?##/ { printf "  %-20s %s\n", $$1, $$NF }' $(MAKEFILE_LIST) | sort

.DEFAULT_GOAL := help
