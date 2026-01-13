Pants Python Monorepo
==============

This is a Python Monorepo example using [Pants Build Sytem](https://www.pantsbuild.org/) and `uv`.
It demonstrates how to manage multiple FastAPI microservices and shared libraries within a single repository, leveraging Pants for efficient dependency usage, caching, and testing.

# Installation

1. First, clone this repository:

```bash
git clone https://github.com/nietzscheson/pants
cd pants
```

2. Resolve dependencies and generate lockfiles:

```bash
pants generate-lockfiles
```

# Usage

## Running Applications

You can run individual applications using the `pants run` command.

**App 1:**

```bash
pants run apps/app_1:app -- apps.app_1.main:app --host 0.0.0.0 --port 8001 --reload
```

The application will be available at: [http://localhost:8001](http://localhost:8001)

## Testing

Run all tests in the repository:

```bash
pants test ::
```

Run tests for a specific app:

```bash
pants test apps/app_1/tests/test_main.py
```

## Linting and Type Checking

The repository is configured with `ruff`, `black`, `isort`, and type checkers.

```bash
# Lint all files
pants lint ::

# Check types
pants check ::
```

## Dependency Management

To add a new dependency, use `uv` or modify `pyproject.toml` manually:

**Using uv:**

```bash
uv add <dependency>
# For dev dependencies
uv add --dev <dependency>
```

**After adding the dependency:**

1.  Regenerate the Pants lockfiles:

```bash
pants generate-lockfiles
```

2.  Import the package in your python code. Pants will automatically infer the dependency for your target.

# Project Structure

```bash
.
├── apps/
│   └── app_1/             # Microservice App 1
│       ├── src/           # Application Source Code
│       └── tests/         # Application Tests
├── 3rdparty/              # Dependency Lockfiles
├── pants.toml             # Pants Configuration
└── pyproject.toml         # Project Dependencies
```