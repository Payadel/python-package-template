.PHONY: help update-poetry-dependencies publish-test-action publish-action tox-action coverage-action

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
