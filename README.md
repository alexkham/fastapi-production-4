# fastapi-production-4
# deployment version
# building docker container from image
 sudo docker build -t my-fastapi-app .  
# start running the container
sudo docker run -d -p 8001:8001 --name fastapi-container my-fastapi-app
