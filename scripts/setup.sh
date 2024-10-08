python -m venv .venv
source .venv/bin/activate
poetry install
cp .bot-env-dev-example .bot-env-dev
cp .bot-env-prod-example .bot-env-prod-example
