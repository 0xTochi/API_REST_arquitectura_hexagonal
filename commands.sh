## LEVANTAR LA API EN DOCKER

docker-compose -f docker-compose.yml up -d

# ELIMINANDO CONTENEDORES HUERFANOS

docker-compose -f docker-compose.yml up -d --remove-orphans

## RESET TODO

docker system prune -a --volumes


