# fastapi-production-4
# deployment version
# building docker container from image
 sudo docker build -t my-fastapi-app .  
# start running the container
sudo docker run -d -p 8001:8001 --name fastapi-container my-fastapi-app

now i run my fastapi app on vps with docker container i need to pull updated code from github and update it on vps so it can run with new code what is exact actions i need to perform?




**1. Pull the Latest Code from GitHub:**
   SSH into your VPS and navigate to your FastAPI app's project directory. Pull the latest code changes from your GitHub repository.

   ```bash
   cd /path/to/your/app
   git pull
   ```



**2. Stop and Remove the Existing Container:**
   Next, stop and remove the existing Docker container:

   ```bash
   docker stop fastapi-container
   docker rm fastapi-container
   ```



**3. Build a New Docker Image:**
   After pulling the latest code, build a new Docker image as before:

   ```bash
   docker build -t my-fastapi-app .
   ```
**4. Run a New Container with the Updated Image:**
   Finally, run a new Docker container using the updated image with the same name:

   ```bash
   docker run -d -p 8001:8001 --name fastapi-container my-fastapi-app
   ```

This approach allows you to update the code within the same container while keeping the container name constant. It can be beneficial if you want to maintain the same container name for consistency or if you have specific configurations tied to that container name.