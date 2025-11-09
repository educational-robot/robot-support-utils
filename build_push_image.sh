VERSION=v0.0.1
IMAGE_NAME=nguyentrminh/robot-support-utils

docker build -t $IMAGE_NAME:$VERSION .
#docker push $IMAGE_NAME:$VERSION