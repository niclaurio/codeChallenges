# Define your environment and command options
PYTHON = python3
LINTER = black ruff mypy
TEST_DIRS = tests/functional tests/unit

# Install pip-tools, compile all .in files to .txt files, and install dependencies
reqs:
	@echo "Installing pip-tools..."
	$(PYTHON) -m pip install pip-tools
	@echo "Compiling requirements_dev.in to requirements_dev.txt..."
	$(PYTHON) -m piptools compile requirements_dev.in
	@echo "Compiling requirements_test.in to requirements_test.txt..."
	$(PYTHON) -m piptools compile requirements_test.in
	@echo "Installing development dependencies from requirements_dev.txt..."
	$(PYTHON) -m pip install -r requirements_dev.txt
	@echo "Installing testing dependencies from requirements_test.txt..."
	$(PYTHON) -m pip install -r requirements_test.txt

# Linter command that runs black, ruff, and mypy
lint:
	@echo "Running linters (black, ruff, mypy)..."
	$(PYTHON) -m mypy .
	$(PYTHON) -m black --check .
	$(PYTHON) -m ruff .

# Tests command to run pytest tests under functional and unit directories
tests:
	@echo "Running tests under functional and unit directories..."
	$(PYTHON) -m pytest $(TEST_DIRS)

# 'all' command to run reqs, lint, and tests in sequence
all: reqs lint tests
	@echo "All tasks (reqs, lint, tests) completed."

# Additional useful Makefile commands
# You can add other targets here as needed, e.g., install, clean, etc.

.PHONY: lint tests reqs all
