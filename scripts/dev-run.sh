export $(grep -v '^#' .bot-env-dev | xargs -d '\n')
docker compose --env-file .bot-env-dev up --wait db -d
alembic upgrade head
python bot
