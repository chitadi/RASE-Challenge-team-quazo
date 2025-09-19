
source ./config.sh

if docker ps -a --format '{{.Names}}' | grep -wq "$CONTAINER_NAME"; then
    echo "Container '$CONTAINER_NAME' exist. Running execute command."
    docker exec -it $CONTAINER_NAME bash
else
    echo "Container '$CONTAINER_NAME' does not exist. Running docker."
    docker run -it \
      --gpus all \
      -v ./dataset/:/data/ \
      -v ./src/:/src/ \
      -v ./results/:/results/ \
      --name $CONTAINER_NAME \
      --workdir /src \
      $IMAGE_NAME \
      bash
fi


