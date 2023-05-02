.PHONY: help watch-actions release-action update-poetry-dependencies publish-test-action publish-action tox-action coverage-action

# Variables
REF := $(if $(ref),$(ref),"dev")
VERSION := $(if $(version),$(version),"")
IGNORE_SAME_VERSION_ERROR := $(if $(ignore-same-version-error),$(ignore-same-version-error),false)
IGNORE_LESS_VERSION_ERROR := $(if $(ignore-less-version-error),$(ignore-less-version-error),false)
CREATE_PR_FOR_BRANCH := $(if $(create-pr-for-branch),$(create-pr-for-branch),"")
GENERATE_CHANGELOG := $(if $(generate-changelog),$(generate-changelog),'auto')
SKIP_RELEASE_FILE := $(if $(skip-release-file),$(skip-release-file),true)
RELEASE_FILE_NAME := $(if $(release-file-name),$(release-file-name),"release")
RELEASE_DIRECTORY := $(if $(release-directory),$(release-directory),".")

# Targets for running workflow commands
watch-actions: ## Watch a run until it completes, showing its progress
	gh run watch; notify-send "run is done!"

release-action: ## Run release action
	gh workflow run Release --ref $(REF) \
		-f version=$(VERSION) \
		-f ignore-same-version-error=$(IGNORE_SAME_VERSION_ERROR) \
		-f ignore-less-version-error=$(IGNORE_LESS_VERSION_ERROR) \
		-f create-pr-for-branch=$(CREATE_PR_FOR_BRANCH) \
		-f generate-changelog=$(GENERATE_CHANGELOG) \
		-f skip-release-file=$(SKIP_RELEASE_FILE) \
		-f release-file-name=$(RELEASE_FILE_NAME) \
		-f release-directory=$(RELEASE_DIRECTORY)

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
