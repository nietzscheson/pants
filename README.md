# Pants + UV (python) integration

1. pants tailor ::
2. pants generate-lockfiles --resolve=python-default
3. pants run src:app -- src.main:app --host 0.0.0.0 --port 8001 --reload 