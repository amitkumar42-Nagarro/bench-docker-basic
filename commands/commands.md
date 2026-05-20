# List of all docker command executed

### docker --version
>![alt text](image.png)

### docker images
>![alt text](image-1.png)

### docker ps
>![alt text](image-2.png)

### docker ps -a
>![alt text](image-3.png)

### docker rmi  &nbsp;&nbsp;(*forced*)
>![alt text](image-4.png)
>![alt text](image-5.png)

### docker rm   &nbsp;&nbsp;(*forced*)
>![alt text](image-6.png)
>![alt text](image-7.png)

### docker rm &nbsp;&nbsp;(*Remove all containers*)
>![alt text](image-8.png)
>![alt text](image-9.png)

### docker rmi &nbsp;&nbsp;(*Remove all images*)
>![alt text](image-10.png)
>![alt text](image-11.png)

### docker build . &nbsp;&nbsp;(*normal at current folder / directory, no tag*)
![alt text](image-12.png)

### docker build -t demo-backend:v0.1 . &nbsp;&nbsp;(*tagged docker image*)
>![alt text](image-13.png)

### docker build --no-cache -t demo-backend-no-cache:v0.2 ./backend/ &nbsp;&nbsp;(*no cache used, fresh image from source*)
>![alt text](image-14.png)

### docker build -t image_tag-name -f docker-file-name .  &nbsp;&nbsp; (*-f if Dockerfile has custom name*)

### docker run <image_id>  &nbsp;&nbsp;(*container forground run command*)
![alt text](image-15.png)

___
### docker run <image_id>  &nbsp;&nbsp;(*container detached mode run command*)
![alt text](image-16.png)

___
### docker run -d -p <host_computer_port>:<container_service_port> <image_id>  &nbsp;&nbsp;(*container port mapping to host*)
*now app can be accessed in computer on port 8080*
![alt text](image-17.png)

___
### docker exec -it <container_id / name> /bin/sh  &nbsp;&nbsp;(*interacting with container's terminal*)
![alt text](image-19.png)

___
### Accessing app from inside container's terminal
![alt text](image-20.png)
![alt text](image-21.png)

___
### docker stop <container_id or name> 
![alt text](image-22.png)
![alt text](image-23.png)

___
### dcoker images prune  &nbsp;&nbsp;(*dleteing all unused images in one go*)
![alt text](image-24.png)

___
### docker compose build &nbsp;&nbsp;(*Build based on the docker compose file*)
docker compose up -d --build &nbsp;&nbsp;(*Build and start in detached mode*)
![alt text](image-25.png)

___
### docker compose up -d &nbsp;&nbsp;(*Start container in detached mode*) 
![alt text](image-26.png)

___
### docker compose exec <service_name_from_dockerFile> sh &nbsp;&nbsp;(*Log into the running service container*) 
![alt text](image-27.png)

___
### docker run -d -p 5001:5000 --restart=always --name local-registry registry:2 &nbsp;&nbsp;(*Run official local registry*) 
![alt text](image-28.png)

___
### docker tag docker_basics-backend:latest localhost:5001/docker_basic-backend:v0.1 &nbsp;&nbsp;(*Tag existing image for docker registry*) 
![alt text](image-29.png)

___
### docker push localhost:5001/docker_basic-backend:v0.1 &nbsp;&nbsp;(*Push existing image to local registry*) 
![alt text](image-30.png)

___
### curl http://localhost:5000/v2/_catalog &nbsp;&nbsp;(*Verify if images pushed*) 
![alt text](image-31.png)\

___
###  docker run -d -p 5001:5000 localhost:5000/docker_basic-backend:v0.1 &nbsp;&nbsp;(*pull and run image from local*) 
![alt text](image-32.png)