.PHONY: help update-poetry-dependencies publish-test-action publish-action build-action coverage-action

update-poetry-dependencies:  ## Update poetry dependencies
	cat requirements.txt | xargs poetry add

publish-test-action: ## Run publish test action
	gh workflow run 'Publish to Test.PyPI' --ref $(REF) -f version=$(VERSION)

publish-action: ## Run publish action
	gh workflow run 'Publish to PyPI' --ref $(REF) -f version=$(VERSION)

build-action: ## Run build action
	gh workflow run build --ref $(REF)

coverage-action:
	gh workflow run 'Coverage Report' --ref $(REF)

help: ## Display this help message
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@awk -F ':|##' '/^[^\t].+?:.*?##/ { printf "  %-20s %s\n", $$1, $$NF }' $(MAKEFILE_LIST) | sort

.DEFAULT_GOAL := help
