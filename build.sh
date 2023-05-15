HUB=brunomassaini
REPOSITORY=chatgpt-discord-bot
VERSION=latest

docker build . -t $HUB/$REPOSITORY:$VERSION
docker push $HUB/$REPOSITORY:$VERSION