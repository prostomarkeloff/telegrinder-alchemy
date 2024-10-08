python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
cp .bot-env-dev-example .bot-env-dev
cp .bot-env-prod-example .bot-env-prod-example
