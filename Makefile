# Define your environment and command options
PYTHON = python3
LINTER = black ruff mypy
TEST_DIRS = tests/functional tests/unit

# Install pip-tools, compile all .in files to .txt files, and install dependencies
reqs:
	echo "Activating virtualenv and installing dependencies..." >> .makefileLogs/reqs_log.txt 2>&1
	rm -rf .venv && \
	${PYTHON} -m venv .venv && \
	source .venv/bin/activate && \
	$(PYTHON) -m pip install pip-tools && \
	$(PYTHON) -m piptools compile requirements_dev.in && \
	$(PYTHON) -m piptools compile requirements_test.in >> .makefileLogs/reqs_log.txt 2>&1


sync:reqs
	$(PYTHON) -m piptools sync requirements*.txt >> .makefileLogs/sync_log.txt 2>&1

install: reqs
	@echo "Installing development and tests dependencies"
	$(PYTHON) -m pip install -r requirements_dev.txt  && \
	$(PYTHON) -m pip install -r requirements_test.txt >> .makefileLogs/install_log.txt 2>&1

lint:
	echo "Running linters (black, ruff, mypy)..."
	echo "mypy" >> .makefileLogs/lint_log.txt 2>&1 || true
	$(PYTHON) -m mypy . >> .makefileLogs/lint_log.txt 2>&1 || true
	echo "black" >> .makefileLogs/lint_log.txt 2>&1 || true
	$(PYTHON) -m black --check . >> .makefileLogs/lint_log.txt 2>&1 || true
	echo "ruff" >> .makefileLogs/lint_log.txt 2>&1 || true
	ruff check . >> .makefileLogs/lint_log.txt 2>&1 || true

# Tests command to run pytest tests under functional and unit directories
tests:
	@echo "Running tests under functional and unit directories..."
	$(PYTHON) -m pytest $(TEST_DIRS) >> .makefileLogs/test_log.txt 2>&1

# 'all' command to run reqs, lint, and tests in sequence
all: reqs install lint tests
	@echo "All tasks (reqs, install, lint, tests) completed."

# Additional useful Makefile commands
# You can add other targets here as needed, e.g., install, clean, etc.

.PHONY: lint tests reqs all
