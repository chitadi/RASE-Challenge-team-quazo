
source ./config.sh # common variables

docker build -t $IMAGE_NAME -f ./baseline.dockerfile ./empty # empty is for the build context (no files to be shifted into docker)
